#!/usr/bin/env python3
"""
YouTube Chapter Screenshot Pipeline
------------------------------------
Uses Google Gemini to analyse a YouTube video, extracts chapter timestamps,
downloads the video with yt-dlp, and captures a screenshot for each chapter
with ffmpeg.

Usage:
    python3 scripts/youtube_chapters.py <youtube-url> [--name <short-name>]

Requirements:
    GOOGLE_API_KEY environment variable must be set.
    yt-dlp and ffmpeg must be on PATH.

Output:
    llmWiki/rawSources/assets/<short-name>/
        chapter_01_<slug>.png
        chapter_02_<slug>.png
        ...
        chapters.md   ← Gemini analysis summary
"""

import argparse
import json
import os
import re
import subprocess
import sys
import textwrap
from pathlib import Path

from google import genai
from google.genai import types


# ── Paths ─────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
ASSETS_DIR = PROJECT_ROOT / "llmWiki" / "rawSources" / "assets"


# ── Gemini ────────────────────────────────────────────────────────────────────

CHAPTER_PROMPT = textwrap.dedent("""
    Analyse this YouTube video carefully.

    Return a JSON object with this exact structure — no markdown fences, pure JSON:
    {
      "title": "video title",
      "channel": "channel name",
      "duration_seconds": 123,
      "chapters": [
        {
          "index": 1,
          "title": "Chapter title",
          "start_seconds": 0,
          "summary": "2-3 sentence summary of what happens in this chapter"
        }
      ]
    }

    If the video has no explicit chapters, divide it into logical sections of
    roughly equal length (aim for 4-8 sections) based on topic changes.
    The first chapter always starts at 0 seconds.
    Use the actual video content to write accurate summaries.
""").strip()


def gemini_analyse(youtube_url: str) -> dict:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("ERROR: GOOGLE_API_KEY environment variable is not set.")

    client = genai.Client(api_key=api_key)
    print(f"[gemini] Analysing {youtube_url} …")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part(file_data=types.FileData(file_uri=youtube_url)),
            types.Part(text=CHAPTER_PROMPT),
        ],
    )

    raw = response.text.strip()
    # Strip markdown code fences if Gemini wraps anyway
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        print("[gemini] Raw response:\n", raw[:2000])
        sys.exit(f"ERROR: Gemini did not return valid JSON — {exc}")

    return data


# ── yt-dlp ────────────────────────────────────────────────────────────────────

def download_video(youtube_url: str, output_path: Path) -> Path:
    print(f"[yt-dlp] Downloading video to {output_path} …")
    cmd = [
        "yt-dlp",
        "--format", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",
        "--output", str(output_path),
        "--no-playlist",
        youtube_url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr)
        sys.exit("ERROR: yt-dlp failed.")

    # yt-dlp may add .mp4 extension automatically
    if not output_path.exists():
        mp4 = output_path.with_suffix(".mp4")
        if mp4.exists():
            return mp4
        sys.exit(f"ERROR: Expected video file not found at {output_path}")

    return output_path


# ── ffmpeg ────────────────────────────────────────────────────────────────────

def extract_frame(video_path: Path, timestamp_s: float, out_png: Path):
    cmd = [
        "ffmpeg",
        "-ss", str(timestamp_s),
        "-i", str(video_path),
        "-frames:v", "1",
        "-q:v", "2",
        str(out_png),
        "-y",
        "-loglevel", "error",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ffmpeg] WARNING: could not extract frame at {timestamp_s}s — {result.stderr.strip()}")


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:50]


def seconds_to_hms(s: float) -> str:
    s = int(s)
    h, rem = divmod(s, 3600)
    m, sec = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{sec:02d}"


def derive_short_name(youtube_url: str) -> str:
    # Extract video ID and use as fallback short name
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", youtube_url)
    return match.group(1) if match else "video"


# ── Markdown output ───────────────────────────────────────────────────────────

def write_chapters_md(out_dir: Path, data: dict, youtube_url: str):
    lines = [
        f"# {data.get('title', 'Unknown Title')}",
        f"",
        f"**Channel:** {data.get('channel', '—')}  ",
        f"**URL:** {youtube_url}  ",
        f"**Duration:** {seconds_to_hms(data.get('duration_seconds', 0))}",
        f"",
        f"---",
        f"",
        f"## Chapters",
        f"",
    ]

    for ch in data.get("chapters", []):
        idx = ch["index"]
        ts = seconds_to_hms(ch["start_seconds"])
        slug = slugify(ch["title"])
        screenshot = f"chapter_{idx:02d}_{slug}.png"
        lines += [
            f"### {idx}. {ch['title']} `[{ts}]`",
            f"",
            f"![{ch['title']}]({screenshot})",
            f"",
            ch["summary"],
            f"",
        ]

    md_path = out_dir / "chapters.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[output] Written {md_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="YouTube chapter screenshot pipeline")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--name", help="Short name for output folder (default: video ID)")
    args = parser.parse_args()

    youtube_url = args.url
    short_name = args.name or derive_short_name(youtube_url)

    out_dir = ASSETS_DIR / short_name
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[setup] Output directory: {out_dir}")

    # 1. Gemini analysis
    data = gemini_analyse(youtube_url)
    chapters = data.get("chapters", [])
    print(f"[gemini] Found {len(chapters)} chapters in '{data.get('title', '?')}'")
    for ch in chapters:
        print(f"         {ch['index']:2d}. [{seconds_to_hms(ch['start_seconds'])}] {ch['title']}")

    # 2. Download video
    video_path = out_dir / f"{short_name}.mp4"
    video_path = download_video(youtube_url, video_path)

    # Get actual video duration from the downloaded file
    probe = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(video_path)],
        capture_output=True, text=True,
    )
    actual_duration = float(probe.stdout.strip()) if probe.stdout.strip() else float("inf")
    print(f"[ffprobe] Video duration: {seconds_to_hms(actual_duration)}")

    # Filter out any chapters whose timestamps exceed the video length
    valid_chapters = [ch for ch in chapters if ch["start_seconds"] < actual_duration - 1]
    skipped = len(chapters) - len(valid_chapters)
    if skipped:
        print(f"[warn] Skipping {skipped} chapter(s) with timestamps beyond video duration")
    chapters = valid_chapters

    # 3. Extract frames — clear any stale chapter PNGs first
    for old_png in out_dir.glob("chapter_*.png"):
        old_png.unlink()
    print("[ffmpeg] Extracting chapter screenshots …")
    for ch in chapters:
        slug = slugify(ch["title"])
        out_png = out_dir / f"chapter_{ch['index']:02d}_{slug}.png"
        seek_s = min(ch["start_seconds"] + 1.5, actual_duration - 1)
        extract_frame(video_path, seek_s, out_png)
        print(f"[ffmpeg] {out_png.name}")

    # 4. Write markdown summary (use only valid chapters)
    data["chapters"] = chapters
    write_chapters_md(out_dir, data, youtube_url)

    print(f"\nDone! {len(chapters)} screenshots saved to {out_dir}")


if __name__ == "__main__":
    main()

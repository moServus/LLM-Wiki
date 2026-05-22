# ML/AI Wiki — Schema & Agent Instructions

This is the authoritative schema for the ML/AI LLM Wiki. Read this file at the start of every session before touching any wiki files.

---

## Directory layout

```
llmWiki/
  CLAUDE.md              ← this file (schema + agent instructions)
  rawSources/            ← immutable source documents (never modify)
    assets-weblinks.md   ← registry of web URLs and YouTube links (queue + status)
    assets/              ← locally downloaded images referenced by sources
    <short-name>.md      ← fetched web pages or YouTube transcripts saved here
  wiki/                  ← LLM-owned, LLM-maintained markdown pages
    index.md             ← master catalog in English (update on every ingest)
    log.md               ← append-only operation log (English only)
    overview.md          ← high-level synthesis (English master)
    concepts/            ← ML/AI concept pages (attention, backprop, RLHF…)
    models/              ← architecture/system pages (GPT-4, Gemini, Llama…)
    papers/              ← one page per ingested paper or article
    people/              ← researchers, labs, key figures
    datasets/            ← dataset and benchmark pages
    comparisons/         ← comparison tables, head-to-head analyses
    translations/        ← all non-English translations
      de/                ← German (mirrors English structure)
        index.md, overview.md, concepts/, models/, papers/, people/, …
      fr/                ← French
      it/                ← Italian
      es/                ← Spanish
```

**Rule:** the LLM may only write/edit files inside `wiki/`. `rawSources/` is read-only, **with one exception**: the LLM may update the `status` column in `rawSources/assets-weblinks.md` after fetching a URL, and may write the fetched content to `rawSources/<short-name>.md`.

---

## Multilingual output

**English is always the master language.** Every wiki page is written in English first. Translations are derived from the English master — never written independently.

### Language directories

| Directory | Language |
|-----------|----------|
| `wiki/` (root) | English — master |
| `wiki/translations/de/` | Deutsch (German) |
| `wiki/translations/fr/` | Français (French) |
| `wiki/translations/it/` | Italiano (Italian) |
| `wiki/translations/es/` | Español (Spanish) |

Each language directory mirrors the English structure exactly: same filenames, same subdirectories (`concepts/`, `models/`, `papers/`, `people/`, `datasets/`, `comparisons/`), plus its own `index.md` and `overview.md`.

`log.md` is **not** translated — it is an operational record, English only.

### Translation rules

- Translate all headings, body text, table content, and TL;DRs into the target language
- Keep the following in English (untranslated): filenames, `[[wikilinks]]`, YAML frontmatter keys, code blocks, proper nouns (model names, dataset names, tool names), and technical terms that have no standard translation in the field (e.g. "fine-tuning", "benchmark")
- Technical terms that *do* have standard translations should use them (e.g. German: "Aufmerksamkeitsmechanismus" for attention mechanism, but "Transformer" stays as-is)
- Wikilinks use the same English slugs everywhere — `[[attention-mechanism]]` not `[[aufmerksamkeitsmechanismus]]`

### When to translate

After completing all English pages during an ingest, translate every new or significantly updated page into all four languages. Minor English edits (typo fixes, one-line additions) do not require re-translating.

---

## Page frontmatter

**English master pages:**

```yaml
---
title: "Human-readable title"
type: concept | model | paper | person | dataset | comparison | overview
tags: [tag1, tag2]
sources: [filename-in-rawSources.md]   # omit if not source-derived
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

**Translated pages** add two fields:

```yaml
---
title: "Translated title"
type: concept | model | paper | person | dataset | comparison | overview
tags: [tag1, tag2]
sources: [filename-in-rawSources.md]
lang: de | fr | it | es
translation_of: "../../concepts/page-slug"   # relative path to English master
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

---

## Wiki page types and conventions

### `concepts/` — ML/AI concept pages
- One page per distinct concept (e.g., `attention-mechanism.md`, `rlhf.md`)
- Structure: **Definition** → **How it works** → **Key variants** → **Related concepts** → **Sources**
- Use `[[wikilink]]` syntax for cross-references to other wiki pages
- Include a short TL;DR summary at the top (2–3 sentences)

### `models/` — Model/system pages
- One page per model family or major version (e.g., `gpt-4.md`, `llama-3.md`)
- Structure: **Overview** → **Architecture** → **Training** → **Benchmarks** → **Notable capabilities/limitations** → **Related models** → **Sources**

### `papers/` — Source summary pages
- One page per ingested paper or article (filename mirrors the rawSource file)
- Structure: **Citation** → **TL;DR** → **Key contributions** → **Methods** → **Results** → **Limitations** → **Wiki impact** (which pages were updated)

### `people/` — Researcher/lab pages
- Key figures and organizations (e.g., `ilya-sutskever.md`, `deepmind.md`)
- Structure: **Role** → **Key contributions** → **Affiliated works** → **Related people/orgs**

### `datasets/` — Dataset/benchmark pages
- Structure: **Description** → **Size & format** → **Common uses** → **Leaderboard snapshot** → **Sources**

### `comparisons/` — Analysis pages
- Generated in response to queries, then filed here
- Must cite the wiki pages they draw from

---

## Operations

### Fetch a web source

Used when the source is a URL rather than an existing file in `rawSources/`.

1. Open `rawSources/assets-weblinks.md` and find the entry (or add it if the user provides a new URL).
2. Fetch the URL and convert the content to clean markdown.
3. Save the result to `rawSources/<short-name>.md` where `<short-name>` matches the entry in the registry (kebab-case, descriptive, e.g. `attention-is-all-you-need`).
4. Update the entry's `status` to `fetched` and set `fetched` date in `assets-weblinks.md`.
5. Proceed with the standard **Ingest a new source** workflow using the saved file.

**Short-name rules:** lowercase, kebab-case, ≤40 chars, no dates unless disambiguation is needed. Should match what a reader would search for.

### Fetch a YouTube source

Used when the source is a YouTube URL. Requires `yt-dlp` (installed via `brew install yt-dlp`).

1. Open `rawSources/assets-weblinks.md` and find or add the entry.
2. Download the transcript/subtitles only (no video):
   ```bash
   yt-dlp --write-auto-sub --skip-download --sub-lang en \
     --convert-subs srt \
     --output "rawSources/<short-name>" \
     "<youtube-url>"
   ```
3. The `.en.srt` file is timestamped plain text. Convert it to clean markdown by stripping timestamps and sequence numbers, then save as `rawSources/<short-name>.md`.
4. Also fetch the video metadata (title, channel, description, chapters):
   ```bash
   yt-dlp --dump-json --skip-download "<youtube-url>"
   ```
   Include title, channel, upload date, and chapter markers at the top of the saved `.md` file.
5. If translations are requested, translate the cleaned transcript into the target languages (German, French, Italian, Spanish) and append each as a `## <Language>` section in the same `rawSources/<short-name>.md` file.
6. Update `assets-weblinks.md` status to `fetched`, then proceed with **Ingest a new source**.

**Note on missing captions:** If `yt-dlp` reports no subtitles available, fall back to `WebFetch` on the YouTube URL to capture the description and any partial transcript shown in the page. Note the limitation in the `rawSources/<short-name>.md` header.

### Ingest a new source

1. Read `wiki/index.md` to understand the current wiki state.
2. Read the source document in `rawSources/`.
3. Briefly discuss key takeaways with the user before writing anything.
4. Write a summary page in `wiki/papers/` (or the appropriate category).
5. Create or update concept/model/people/dataset pages touched by the source.
6. Update `wiki/index.md` — add the new page(s), update any modified pages.
7. Update `wiki/overview.md` if the source materially shifts the synthesis.
8. Append an entry to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <source title>`

**Touch as many pages as needed.** A single source commonly updates 5–15 pages.

After all English pages are written and updated:

9. Translate every new or significantly updated page into DE, FR, IT, ES and save to the corresponding `wiki/<lang>/` subdirectory.
10. Update `wiki/<lang>/index.md` for each language to reflect new/changed pages.
11. Update `wiki/<lang>/overview.md` for each language if the English overview changed.

### Answer a query

1. Read `wiki/index.md` to identify relevant pages.
2. Read those pages and synthesize an answer with citations (`[[page]]`).
3. If the answer is substantial (comparison, analysis, new synthesis), offer to file it as a new page in `wiki/comparisons/` or the appropriate category.
4. Append a log entry: `## [YYYY-MM-DD] query | <question summary>`

### Lint the wiki

1. Scan all pages for: broken `[[wikilinks]]`, orphan pages (no inbound links), contradictions between pages, stale claims, missing cross-references, important concepts mentioned but lacking their own page.
2. Report findings to the user before making any changes.
3. Fix approved issues and append: `## [YYYY-MM-DD] lint | <summary of fixes>`

---

## Cross-referencing rules

- Use `[[filename-without-extension]]` for wikilinks (Obsidian-compatible).
- Every new page must link to at least two existing pages where relevant.
- When a concept first appears on a page, link it — don't repeat the link on subsequent mentions on the same page.

---

## Style guidelines

- Write in clear, precise technical English. Assume a reader with ML fundamentals.
- Prefer concrete examples over abstract descriptions.
- Flag uncertainty: use "reportedly", "as of [date]", or a `> **Note:** ...` blockquote for unverified claims.
- Keep TL;DRs to 2–3 sentences maximum.
- Table of contents is optional for pages under ~500 words; required above that.

---

## Domain scope

This wiki covers **machine learning and AI**, including:
- Core ML concepts (architectures, training methods, optimization, evaluation)
- Foundation models and LLMs (pretraining, fine-tuning, RLHF, inference)
- Multimodal systems (vision-language, speech, video)
- AI safety and alignment
- Benchmarks and evaluation methodology
- Key researchers, labs, and organizations
- Datasets used in ML research

Out of scope: general software engineering, unrelated math, business strategy unconnected to AI.

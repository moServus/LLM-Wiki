# Web & YouTube Link Registry

Queue of URLs to fetch and ingest into the wiki.

**Workflow:** add a row below → tell Claude "fetch next queued link" or "fetch <short-name>" → Claude fetches it, saves to `rawSources/<short-name>.md`, updates status here, then ingests it into the wiki.

| short-name | URL | type | lang | status | added | fetched |
|------------|-----|------|------|--------|-------|---------|
| karpathy-llm-wiki-explained | https://youtu.be/aGXTV5MTqDY | youtube | en → de,fr,it,es | ingested | 2026-05-22 | 2026-05-22 |
| llm-wiki-101 | https://agentpedia.codes/blog/karpathy-llm-wiki-idea-file | web | en | ingested | 2026-05-22 | 2026-05-22 |

---

## Status values

| Value | Meaning |
|-------|---------|
| `queued` | URL added, not yet fetched |
| `fetched` | Saved to `rawSources/<short-name>.md`, ready to ingest |
| `ingested` | Fully processed into the wiki |
| `skip` | Decided not to process |

## Type values

| Value | Meaning |
|-------|---------|
| `web` | Standard web article — fetched via WebFetch |
| `youtube` | YouTube video — transcript extracted via yt-dlp |

## Lang column

Source language of the content (e.g. `en`, `de`, `fr`). For YouTube sources, also note if translations are wanted, e.g. `en → de,fr,it,es`.

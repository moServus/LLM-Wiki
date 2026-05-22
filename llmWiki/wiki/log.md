# Wiki Log

Append-only chronological record of all wiki operations.

Entry format: `## [YYYY-MM-DD] <operation> | <title>`
Operations: `ingest`, `query`, `lint`, `init`

Parse last 5 entries: `grep "^## \[" wiki/log.md | tail -5`

---

## [2026-05-22] schema | Multilingual output workflow added

CLAUDE.md updated: multilingual output section, translation rules, language directories, ingest workflow extended with steps 9–11. Directories created: wiki/de/, wiki/fr/, wiki/it/, wiki/es/ (each with concepts/, models/, papers/, people/, datasets/, comparisons/).
All existing pages backfilled in DE, FR, IT, ES: llm-wiki-pattern, retrieval-augmented-generation, andrej-karpathy, index, overview.
Rule: English is always master; translations follow after English pages are complete; log.md is English-only.

## [2026-05-22] ingest | Karpathy's LLM Wiki Explained — YouTube (AI Simplified)

Source: rawSources/karpathy-llm-wiki-explained.md (YouTube transcript + DE/FR/IT/ES translations)
Pages created: wiki/papers/karpathy-llm-wiki-explained.md
Pages updated: wiki/concepts/llm-wiki-pattern.md (file-back command, lint cadence, IDE framing), wiki/index.md, wiki/overview.md

## [2026-05-22] ingest | Karpathy's LLM Wiki — agentpedia.codes

Source: rawSources/llm-wiki-101.md (fetched from assets-weblinks.md)
Pages created: wiki/papers/llm-wiki-101.md, wiki/concepts/llm-wiki-pattern.md, wiki/concepts/retrieval-augmented-generation.md, wiki/people/andrej-karpathy.md
Pages updated: wiki/index.md, wiki/overview.md

## [2026-05-22] init | ML/AI Wiki initialized

Directory structure created. CLAUDE.md schema written. index.md, log.md, and overview.md scaffolded. No sources ingested yet.

---
title: "Karpathy's LLM Wiki Explained — The Idea File That's Replacing RAG"
type: paper
tags: [llm-wiki, knowledge-management, tutorial, youtube]
sources: [karpathy-llm-wiki-explained.md]
created: 2026-05-22
updated: 2026-05-22
---

# Karpathy's LLM Wiki Explained (YouTube, AI Simplified)

**Citation:** AI Simplified. "Karpathy's LLM Wiki Explained — The Idea File That's Replacing RAG." YouTube, 2026-04-05. https://youtu.be/aGXTV5MTqDY (5:19)

**TL;DR:** A practical walkthrough of setting up the [[llm-wiki-pattern]] from scratch: directory structure, schema file, ingestion workflow, query-and-file loop, and monthly lint pass. Reinforces the same architecture as [[llm-wiki-101]] with more emphasis on step-by-step setup and the "IDE / programmer / codebase" framing.

---

## Key contributions vs. [[llm-wiki-101]]

This source is a video companion to the Karpathy idea file. New emphasis over the written article:

- **Practical setup sequence** — explicit step-by-step: folder → schema.md → index.md + log.md → ingest test → query → lint
- **Schema called `schema.md`** here (vs. `CLAUDE.md` / `AGENTS.md` in the idea file) — same concept, different filename convention
- **"File back" command** — explicitly instructs users to append *"save this synthesis as a new page in the Wiki and link it"* to every query that produces a valuable answer; this is the mechanism for compounding query results
- **Lint pass framed as monthly** — concrete cadence recommendation
- **Memorable framing:** *"Your text editor is the IDE. The AI is the programmer. Your knowledge is the code base."*
- **Available in DE, FR, IT, ES** — full translations in rawSource file

## Methods / workflow shown

```
1. Create rawSources/ + wiki/ directories
2. Write schema.md in root (defines rules + conventions)
3. Create wiki/index.md and wiki/log.md (blank)
4. Drop document into rawSources/
5. Prompt: "ingest [file]"
   → AI writes summary, updates index, appends log entry
6. Prompt: "compare X against Y — save synthesis as new wiki page and link it"
   → Answer filed as permanent page, graph grows
7. Monthly: "run a full health check on the wiki folder"
   → lint pass: broken links, duplicate tags, concept gaps
```

## Limitations / gaps

- 5-minute video; no code shown, no tooling demo
- Does not cover search tooling, image handling, or batch ingestion
- Schema template referenced in description links to a third-party site

## Wiki impact

Pages updated by this ingest:
- [[llm-wiki-pattern]] (updated: file-back command detail, lint cadence, IDE framing)
- [[index]] (updated)
- [[overview]] (updated)
- [[log]] (updated)

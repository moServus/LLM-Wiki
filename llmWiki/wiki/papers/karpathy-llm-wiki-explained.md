---
title: "Karpathy's LLM Wiki Explained — The Idea File That's Replacing RAG"
type: paper
tags: [llm-wiki, knowledge-management, tutorial, youtube]
sources: [karpathy-llm-wiki-explained.md]
created: 2026-05-22
updated: 2026-05-22
assets: [rawSources/assets/karpathy-llm-wiki/]
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

## Video chapters

### 1. The Problem with Temporary AI Chat Sessions `[00:00:00]`

![Chapter 1](../../rawSources/assets/karpathy-llm-wiki/chapter_01_the-problem-with-temporary-ai-chat-sessions.png)

The video highlights the inefficiency of traditional AI chat interfaces where carefully built context is lost after each session, forcing the AI to restart from scratch for complex problems. It proposes building an LLM Wiki as a solution that acts as a persistent bookkeeper for your knowledge.

### 2. Setting Up the LLM Wiki Directory `[00:00:20]`

![Chapter 2](../../rawSources/assets/karpathy-llm-wiki/chapter_02_setting-up-the-llm-wiki-directory.png)

The first step involves creating a master folder with two subfolders: `rawSources/` (read-only for the AI) and `wiki/`. A `schema.md` configuration file placed in the root directory establishes strict rules for directory structure, naming conventions, and file formatting, turning a generic AI into a disciplined archivist.

### 3. AI Navigation and Data Ingestion `[00:02:26]`

![Chapter 3](../../rawSources/assets/karpathy-llm-wiki/chapter_03_ai-navigation-and-data-ingestion.png)

Inside the `wiki/` subfolder, two blank text files — `index.md` and `log.md` — are created. The `log.md` uses a specific Unix-style date format for easy parsing. The ingestion workflow demonstrates how dropping a document into `rawSources/` prompts the AI to read, summarize, cross-reference, and log the entry automatically.

### 4. Querying, Linking, and Database Maintenance `[00:05:10]`

![Chapter 4](../../rawSources/assets/karpathy-llm-wiki/chapter_04_querying-linking-and-database-maintenance.png)

After ingesting sources, users prompt the AI with specific questions, forcing it to compare new documents against existing wiki topics and save the synthesis as a new, linked permanent page. A monthly lint pass prompts the AI to perform a health check — fixing broken links, duplicate tags, and organizational gaps autonomously.

---

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

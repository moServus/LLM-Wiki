---
title: "LLM Wiki Pattern"
type: concept
tags: [knowledge-management, llm, methodology, wiki]
sources: [llm-wiki-101.md]
created: 2026-05-22
updated: 2026-05-22
---

# LLM Wiki Pattern

**TL;DR:** A methodology where an LLM incrementally builds and maintains a persistent wiki of interlinked markdown files from a curated source collection. Knowledge compounds across ingests rather than being re-derived per query, solving the accumulation problem inherent in [[retrieval-augmented-generation]].

---

## Definition

The LLM Wiki pattern replaces per-query retrieval with an LLM-maintained knowledge base. When a source is added, the LLM reads it, extracts key information, and integrates it into an evolving wiki — updating entity pages, revising summaries, flagging contradictions, and strengthening cross-references. The wiki is a **persistent, compounding artifact**.

## Three-layer architecture

```
Raw sources  →  Wiki  →  Schema
(immutable)    (LLM-owned markdown)  (agent config)
```

**Raw sources:** Curated articles, papers, images. Never modified by the LLM. The source of truth.

**Wiki:** LLM-generated and LLM-maintained markdown pages. Concepts, models, entities, comparisons, an overview. The LLM creates pages, updates them on new ingests, and maintains cross-references.

**Schema (CLAUDE.md / AGENTS.md):** Tells the agent how the wiki is structured, what conventions to follow, and which workflows to run. Co-evolved by human and LLM. The key configuration file that makes the agent a disciplined wiki maintainer rather than a generic chatbot.

## Core operations

| Operation | Trigger | Output |
|-----------|---------|--------|
| **Ingest** | New source added | Summary page + 5–15 updated pages + index/log entries |
| **Query** | User question | Synthesized answer; valuable answers filed as new pages |
| **Lint** | Periodic maintenance | Contradiction/orphan/gap report; approved fixes applied |

## Infrastructure files

- **`index.md`:** Content-oriented catalog of all pages with one-line summaries. The agent reads this first on every query to locate relevant pages. Sufficient up to ~200–300 pages without vector embeddings.
- **`log.md`:** Append-only chronological record of every ingest, query, and lint pass. Parseable with `grep "^## \["`.

## Why it works

The maintenance burden of traditional wikis grows faster than their value — humans abandon them. LLMs handle bookkeeping (cross-references, consistency, index updates) without fatigue, at near-zero marginal cost per ingest. The human's job shrinks to: curate sources, ask questions, think about what it means.

## Tool stack (optional)

- **Obsidian** — browse the wiki, graph view, Marp slide export, Dataview queries
- **Obsidian Web Clipper** — convert web articles to markdown for `rawSources/`
- **qmd** — local hybrid BM25/vector search over markdown when index.md becomes insufficient
- **Git** — version history, branching, collaboration

## Intellectual lineage

Karpathy connects the pattern to Vannevar Bush's **Memex** (1945) — a personal knowledge store with associative trails between documents. Bush's unsolved problem was maintenance cost; LLMs resolve this.

## The "file back" command

A key practical technique from the video source: whenever a query produces a valuable answer, append this to the prompt:

> *"Save this synthesis as a new page in the Wiki and link it."*

This is the mechanism that makes query results compound in the wiki rather than disappear into chat history. Every question that produces insight becomes a permanent, linked page.

## Lint cadence

Monthly is the recommended cadence for lint passes (from [[karpathy-llm-wiki-explained]]). Prompt: *"Run a full health check on the wiki folder — look for broken links, duplicate tags, or concepts mentioned frequently but lacking their own page."*

## The IDE framing

> *"Your text editor is the IDE. The AI is the programmer. Your knowledge is the code base."*
> — AI Simplified, 2026

## Related concepts

- [[retrieval-augmented-generation]] — the approach this pattern improves upon for personal knowledge bases
- [[andrej-karpathy]] — originator of the pattern

## Sources

- [[llm-wiki-101]]

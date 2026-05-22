---
title: "Karpathy's LLM Wiki: The Complete Guide to His Idea File"
type: paper
tags: [llm-wiki, knowledge-management, rag, methodology]
sources: [llm-wiki-101.md]
created: 2026-05-22
updated: 2026-05-22
---

# Karpathy's LLM Wiki — Source Summary

**Citation:** agentpedia.codes/blog/karpathy-llm-wiki-idea-file (2026). Commentary on Andrej Karpathy's GitHub gist "LLM Wiki idea file."

**TL;DR:** Karpathy proposes replacing per-query RAG with a persistent, LLM-maintained wiki of interlinked markdown files. Knowledge is compiled once at ingest and compounds over time; the LLM handles all bookkeeping while the human focuses on sourcing and questioning.

---

## Key contributions

- Articulates the core weakness of RAG: knowledge is re-derived from scratch on every query, with no accumulation
- Introduces a three-layer architecture: **raw sources** (immutable) → **wiki** (LLM-owned markdown) → **schema** (agent config file)
- Defines three canonical operations: **ingest**, **query**, **lint**
- Proposes `index.md` + `log.md` as lightweight navigation infrastructure replacing embedding-based retrieval at moderate scale (~100 sources)
- Frames "idea files" as a new knowledge-sharing format: share patterns for AI agents rather than runnable code

## Methods / architecture

| Layer | Owner | Description |
|-------|-------|-------------|
| Raw sources | Human | Immutable articles, papers, data; LLM reads only |
| Wiki | LLM | Markdown pages: concepts, entities, comparisons, overview |
| Schema | Human + LLM co-evolved | CLAUDE.md / AGENTS.md defines structure and workflows |

### Operations
- **Ingest:** read source → discuss takeaways → write summary → update 5–15 cross-linked pages → update index + log
- **Query:** read index → read relevant pages → synthesize answer → optionally file result as new page
- **Lint:** scan for contradictions, orphan pages, missing cross-references, stale claims

## Results / claims

- At ~100 sources / hundreds of pages, `index.md`-based lookup is sufficient without vector embeddings
- LLMs can update 15 files in one pass, solving the maintenance-burden problem that causes humans to abandon wikis
- Valuable query answers filed back into the wiki create a compounding knowledge loop

## Limitations / gaps

- No empirical benchmarks; claims are design-rationale, not measured performance
- Scale ceiling for `index.md`-only navigation is unspecified (community suggests ~200–300 pages before search tools like `qmd` become necessary)
- Image handling remains "clunky" — LLMs cannot read markdown with inline images in one pass

## Wiki impact

Pages created or updated by this ingest:
- [[llm-wiki-pattern]] (new concept page)
- [[retrieval-augmented-generation]] (new concept page)
- [[andrej-karpathy]] (new person page)
- [[index]] (updated)
- [[overview]] (updated)

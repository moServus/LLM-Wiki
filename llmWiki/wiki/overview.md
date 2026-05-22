---
title: "ML/AI Wiki — Overview"
type: overview
tags: [overview, synthesis]
sources: [llm-wiki-101.md]
created: 2026-05-22
updated: 2026-05-22
---

# ML/AI Wiki — Overview

**TL;DR:** This wiki is a living synthesis of machine learning and AI research. It currently covers knowledge management methodology for LLM-based wikis and foundational retrieval concepts. It will grow with each ingested source.

---

## State of the wiki

2 sources ingested (2026-05-22). 5 substantive pages: 2 concepts, 1 person, 2 paper summaries.

---

## Major themes

### Knowledge management with LLMs
The opening source establishes the [[llm-wiki-pattern]] as the methodology for this wiki itself — a meta-source. The core tension documented is **RAG vs. persistent wiki**: RAG re-derives knowledge per query; the wiki compiles it once and compounds it across ingests. See [[retrieval-augmented-generation]] for the baseline approach this pattern improves upon.

---

## Key open questions

- At what source/page count does `index.md`-only navigation break down, and what search tooling (e.g. `qmd`) is needed?
- How should contradictions between sources be surfaced and resolved in practice?
- What page granularity works best — one page per concept, or merged topic pages?

---

## Recent developments

- **2026-05-22:** Wiki initialized. Two sources ingested: Karpathy LLM Wiki article + YouTube walkthrough (DE/FR/IT/ES translations). Pages created for [[llm-wiki-pattern]], [[retrieval-augmented-generation]], [[andrej-karpathy]]. [[llm-wiki-pattern]] updated with file-back command detail and monthly lint cadence.

---

## Navigation

- [[index]] — full page catalog
- [[log]] — operation history

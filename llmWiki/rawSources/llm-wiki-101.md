# Karpathy's LLM Wiki: The Complete Guide to His Idea File

Source: https://agentpedia.codes/blog/karpathy-llm-wiki-idea-file
Fetched: 2026-05-22

---

## Overview

Andrej Karpathy introduced an "idea file" — a GitHub gist outlining how to build personal knowledge wikis using LLMs instead of traditional RAG systems. Rather than sharing specific code, this new format lets AI agents customize implementations for individual needs.

## Core Concept: Wiki Over RAG

The fundamental shift moves away from retrieval-augmented generation toward persistent, structured wikis. As explained, "The LLM is rediscovering knowledge from scratch on every question. There's no accumulation" with RAG. Karpathy's approach has LLMs incrementally build and maintain interlinked markdown files that compound knowledge over time.

Key advantages:
- **Processing**: Knowledge compiled once at ingest, not re-derived per query
- **Maintenance**: LLMs handle cross-references automatically
- **Persistence**: Output exists as durable markdown files
- **Synthesis**: Contradictions and connections are pre-built

## Three-Layer Architecture

**Layer 1 — Raw Sources**: Immutable collection of articles, papers, images, and data files the LLM reads but never modifies.

**Layer 2 — The Wiki**: LLM-generated markdown directory containing summaries, entity pages, concept articles, and comparisons maintained entirely by the AI.

**Layer 3 — The Schema**: Configuration file (CLAUDE.md, AGENTS.md) defining wiki structure, conventions, and workflows so the LLM operates consistently.

## Core Operations

**Ingest**: Drop sources into the raw collection; the LLM processes them, writes summaries, updates relevant pages, maintains the index, and logs activity.

**Query**: Ask questions; the LLM synthesizes answers from wiki pages. Valuable responses get filed back as new wiki pages, creating a compounding loop.

**Lint**: Periodically health-check the wiki for contradictions, orphaned pages, missing concepts, and suggest investigations.

## Tool Stack

- **Obsidian**: IDE for browsing the wiki
- **qmd**: Local markdown search engine with hybrid BM25/vector search
- **Web Clipper**: Browser extension converting articles to markdown
- **Marp**: Generate slide decks from wiki content
- **Dataview**: Query page frontmatter for dynamic tables
- **Git**: Version control and collaboration

## Special Files

**index.md**: Content-oriented catalog listing all pages by category with summaries. Replaces embedding-based RAG at moderate scale.

**log.md**: Append-only chronological record of ingests, queries, and maintenance. Parseable with simple text tools.

## Use Cases

- Personal knowledge bases (goals, health, psychology)
- Research projects building evolving theses
- Book companions tracking characters and themes
- Business/team knowledge systems fed by Slack, transcripts, and documents
- Competitive analysis, due diligence, course notes

## The Memex Connection

Karpathy traces intellectual lineage to Vannevar Bush's 1945 "Memex" — a personal knowledge store with associative trails between documents. Bush's missing piece: "who does the maintenance?" LLMs solve this because they handle bookkeeping without fatigue.

## Idea Files as a Format

This represents a paradigm shift in knowledge sharing. Rather than distributing specific code implementations, developers share patterns designed for AI agents to interpret and customize. The gist explicitly states its job: "communicate the pattern. Your LLM can figure out the rest."

## Implementation Path

1. Create directory structure (raw/, wiki/ with subdirectories)
2. Write a schema file defining conventions
3. Configure Obsidian and Web Clipper
4. Ingest 10-20 sources on one topic
5. Query the wiki; file valuable insights back
6. Run lint checks weekly
7. Evolve the schema based on experience

## Community Extensions

Contributors have added patterns including:
- `.brain` folders for project-specific persistent memory
- GitHub gists as inter-agent communication channels
- Team knowledge sharing via shared repositories
- Integration with MCP servers for broader assistant access

## Key Insight

The approach succeeds because "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping." LLMs excel at this invisible work, letting human attention focus on sourcing and questioning rather than administrative overhead.

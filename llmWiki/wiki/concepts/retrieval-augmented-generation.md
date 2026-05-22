---
title: "Retrieval-Augmented Generation (RAG)"
type: concept
tags: [rag, retrieval, llm, knowledge, architecture]
sources: [llm-wiki-101.md]
created: 2026-05-22
updated: 2026-05-22
---

# Retrieval-Augmented Generation (RAG)

**TL;DR:** RAG grounds LLM responses by retrieving relevant document chunks at query time and including them in the context window. It is the dominant approach for document Q&A but has a key weakness: knowledge is re-derived from scratch on every query with no accumulation across sessions.

---

## Definition

RAG is a technique that augments an LLM's generation with retrieved context from an external corpus. At query time, a retrieval system (typically embedding-based vector search) fetches the most relevant chunks from a document collection; those chunks are prepended to the prompt, and the LLM generates an answer grounded in them.

## How it works

```
Query
  ↓
Embed query → vector similarity search over indexed chunks
  ↓
Retrieve top-k chunks
  ↓
Prompt = system + retrieved chunks + query
  ↓
LLM generates grounded answer
```

## Key variants

| Variant | Description |
|---------|-------------|
| Naive RAG | Single-step retrieve-then-generate |
| HyDE | Generate a hypothetical answer, embed it, retrieve similar chunks |
| Re-ranking | Two-stage: fast retrieval then cross-encoder rerank |
| Multi-hop RAG | Iterative retrieval steps for questions requiring multiple reasoning steps |
| Agentic RAG | LLM decides when and what to retrieve during generation |

## Strengths

- Works on any corpus without fine-tuning the LLM
- Knowledge can be updated by updating the index without retraining
- Grounding reduces hallucination on factual questions
- Scales to large document collections with efficient approximate nearest-neighbour search

## Limitations

- **No accumulation:** the LLM re-discovers knowledge from scratch on every query; cross-document synthesis must be redone each time
- **Chunk boundary problem:** relevant information may straddle chunk boundaries and be partially retrieved
- **Retrieval quality ceiling:** the LLM cannot reason about information it failed to retrieve
- **Infrastructure overhead:** requires embedding model, vector store, and indexing pipeline
- **Latency:** retrieval adds a round-trip before generation

## RAG vs. LLM Wiki Pattern

| Dimension | RAG | [[llm-wiki-pattern]] |
|-----------|-----|---------------------|
| Knowledge compilation | Per query | At ingest (once) |
| Cross-document synthesis | Re-derived each time | Pre-built into wiki pages |
| Contradiction detection | None | Flagged during ingest |
| Infrastructure | Vector store + embeddings | Flat markdown files |
| Scale ceiling | Very high | ~200–300 pages before search tools needed |
| Human effort | Low (upload docs) | Higher (curation + review) |

The [[llm-wiki-pattern]] is not a replacement for RAG in general; it is better suited to **personal, curated, actively-maintained** knowledge bases where accumulation and synthesis matter more than scale.

## Common implementations

- LangChain / LlamaIndex (Python)
- OpenAI Assistants API file search
- NotebookLM (Google)
- Perplexity (web-scale)

## Related concepts

- [[llm-wiki-pattern]] — alternative architecture for personal knowledge bases

## Sources

- [[llm-wiki-101]]

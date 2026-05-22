# Daily Workflow Integration

> How to make your LLM Wiki part of your everyday rhythm — without it becoming a chore.

---

## The Core Principle: Capture First, Organize Later

The biggest mistake people make with a personal wiki is spending more time organizing it than using it. The rule is simple: **low friction to add, high reward to browse**.

Write messy notes. Link them later. The graph will make sense over time.

---

## A Daily Routine That Works

### Morning (5–10 min) — Scan & Orient

Start your day by glancing at:

- Your wiki's **Recent Changes** or commit log — what did you add yesterday?
- The **network graph** — is there a cluster you've been neglecting?
- One unfinished stub page — can you add two sentences?

This isn't deep work. It's just keeping the mental map warm.

---

### During Research (ongoing) — Capture as You Go

Whenever you read a paper, article, or watch a talk:

1. Open a new `.md` file in `wiki/`
2. Write 3–5 bullet points of what you learned
3. Add at least one `[[wikilink]]` to a concept you already have
4. Commit with a short message: `add: notes on LoRA fine-tuning`

You don't need a perfect page. A stub with two lines and one link is infinitely better than nothing.

**Capture triggers to watch for:**

- "I didn't know that" → write it down
- "This reminds me of X" → create a link
- "I want to come back to this" → create a stub
- "I'm not sure about Y" → create a question page

---

### During Experiments (as needed) — Log Observations

When you run a model, try a prompt technique, or test a tool:

```markdown
## Experiment: Chain-of-thought on math problems
**Date:** 2026-05-22
**Model:** Claude Sonnet
**Observation:** Adding "think step by step" reduced errors by ~40% on 5-step arithmetic
**See also:** [[chain-of-thought-prompting]], [[few-shot-learning]]
```

These logs become incredibly valuable three months later when you can't remember what you tested.

---

### Weekly (15–20 min) — Connect & Prune

Once a week, do a light maintenance pass:

1. **Link orphans** — find pages with no incoming links and connect them
2. **Merge stubs** — combine two thin pages that are really the same concept
3. **Update the graph data** — add new nodes/edges to `docs/graph-data.js` so the visualization stays current
4. **Write one "synthesis" note** — a page that explains how 3+ concepts relate to each other

Synthesis pages are the most valuable pages in any wiki. They're where understanding crystallizes.

---

## Workflow by Use Case

### If you're a developer

Focus your wiki on: model APIs, prompt engineering patterns, retrieval systems, evaluation methods, deployment strategies. Connect each tool you use to the underlying concepts it implements.

### If you're a researcher

Focus on: paper summaries, method comparisons, benchmark results, open problems, and the genealogy of ideas (which paper builds on which).

### If you're a practitioner / business user

Focus on: use case patterns, prompting techniques, tool comparisons, risk and reliability notes, cost/performance tradeoffs.

### If you're a learner

Start with the fundamentals cluster (transformers, attention, tokenization, embeddings) and build outward. Let curiosity guide the edges.

---

## The 2-Minute Rule for Wikis

If you can add something in under 2 minutes, do it now. A one-line stub, a link between two pages, a renamed heading. These micro-contributions compound into a rich knowledge base over months.

If it'll take more than 2 minutes, create a stub with a `TODO` and come back later.

---

## Avoiding Wiki Rot

Wikis die when they become stale. Signs of wiki rot:

- Pages that say "to be written" for months
- A graph that hasn't changed in weeks
- Notes that feel like they're from a different era of the field

Counter-measures:
- Delete stubs older than 60 days if you never filled them in
- Review your oldest pages quarterly — the field moves fast
- Keep a `CHANGELOG.md` so you can see the wiki's evolution

---

## Related Pages

- [What is an LLM Wiki?](what-is-llm-wiki.md)
- [Tools & Setup Guide](tools-setup.md)
- [Concepts Map](concepts-map.md)

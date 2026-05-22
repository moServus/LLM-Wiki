# 🧠 LLM Wiki

> A personal knowledge base for understanding and using Large Language Models in daily life — with an interactive concept map.

[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://your-username.github.io/llm-wiki)

---

## What's Inside

| Page | Description |
|------|-------------|
| [What is an LLM Wiki?](wiki/what-is-llm-wiki.md) | Concept, purpose, and why it matters |
| [Daily Workflow Integration](wiki/daily-workflow.md) | How to use it as a living knowledge base |
| [Tools & Setup Guide](wiki/tools-setup.md) | GitHub, Obsidian, static sites, and more |
| [Concepts Map](wiki/concepts-map.md) | How LLM topics connect to each other |

## Interactive Network Graph

The **[live concept graph](https://your-username.github.io/llm-wiki)** visualizes how topics in this wiki connect — built with D3.js and hosted on GitHub Pages.

To view it locally, open `docs/index.html` in a browser.

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/your-username/llm-wiki.git
cd llm-wiki

# View the graph locally
open docs/index.html
```

## Contributing / Adding Pages

1. Create a new `.md` file in `wiki/`
2. Add a node + edges to `docs/graph-data.js`
3. Link it from `README.md`
4. Push — GitHub Pages updates automatically

---

## Structure

```
llm-wiki/
├── README.md                  # You are here
├── wiki/
│   ├── what-is-llm-wiki.md
│   ├── daily-workflow.md
│   ├── tools-setup.md
│   └── concepts-map.md
├── docs/                      # GitHub Pages root
│   ├── index.html             # Interactive network graph
│   ├── graph-data.js          # Node/edge data for the graph
│   └── _config.yml            # GitHub Pages config
└── .github/
    └── workflows/
        └── pages.yml          # Auto-deploy on push
```

---

*Built with [D3.js](https://d3js.org) · Hosted on [GitHub Pages](https://pages.github.com)*

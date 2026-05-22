# Tools & Setup Guide

> Everything you need to get your LLM Wiki running locally and published on GitHub Pages.

---

## The Full Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Storage | Git + GitHub | Version control, collaboration |
| Writing | VS Code or Obsidian | Editing markdown files |
| Visualization | D3.js (this repo) | Interactive concept graph |
| Publishing | GitHub Pages | Free static site hosting |
| Navigation | GitHub UI | Browse wiki on github.com |

You can adopt all of these or just the ones that fit your workflow.

---

## 1. GitHub Repository Setup

### Create the repo

1. Go to [github.com/new](https://github.com/new)
2. Name it `llm-wiki` (or anything you like)
3. Set it to **Public** (required for free GitHub Pages)
4. Do **not** initialize with a README (you already have one)
5. Click **Create repository**

### Push your local wiki

```bash
cd "path/to/LLM Wiki"

# Initialize git
git init
git add .
git commit -m "initial: LLM wiki with concept graph"

# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/llm-wiki.git
git branch -M main
git push -u origin main
```

---

## 2. GitHub Pages Setup

GitHub Pages will serve your `docs/` folder as a website at `https://your-username.github.io/llm-wiki`.

### Enable GitHub Pages

1. Go to your repo on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. Under **Source**, select **Deploy from a branch**
4. Branch: `main` | Folder: `/docs`
5. Click **Save**

Within a minute, your concept graph will be live.

### Update your README links

In `README.md`, replace `your-username` with your actual GitHub username:

```markdown
[![GitHub Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://YOUR_USERNAME.github.io/llm-wiki)
```

---

## 3. Writing Tool: VS Code

VS Code is the simplest option — no extra setup required.

**Recommended extensions:**

- **Markdown Preview Enhanced** — live preview of `.md` files
- **GitLens** — see who changed what, when
- **Foam** (optional) — adds `[[wikilink]]` support and a graph view inside VS Code

### Useful keyboard shortcuts

| Action | Shortcut (Mac) |
|--------|----------------|
| Preview markdown | `Cmd + Shift + V` |
| Open file quickly | `Cmd + P` |
| Multi-file search | `Cmd + Shift + F` |

---

## 4. Writing Tool: Obsidian (optional, powerful)

[Obsidian](https://obsidian.md) is a dedicated markdown knowledge base app with a built-in graph view.

### Setup

1. Download and install Obsidian (free)
2. Open Obsidian → **Open folder as vault**
3. Select your `wiki/` folder
4. Obsidian will auto-detect links and build its own graph

### Why use Obsidian alongside GitHub?

Obsidian gives you a beautiful local graph and a distraction-free writing environment. GitHub gives you version history, sharing, and the web-based graph. They complement each other perfectly.

**Tip:** Set Obsidian's new note folder to `wiki/` so files always end up in the right place.

---

## 5. Adding New Concepts to the Graph

The interactive graph at `docs/index.html` reads its data from `docs/graph-data.js`. When you add a new wiki page, add its node here too.

### Open `docs/graph-data.js` and add your node:

```javascript
// In the nodes array:
{ id: "your-concept", label: "Your Concept", group: "core", url: "../wiki/your-concept.md" },

// In the links array (connect to related nodes):
{ source: "your-concept", target: "transformers", label: "uses" },
{ source: "your-concept", target: "fine-tuning", label: "enables" },
```

**Groups available:**

| Group | Color | Use for |
|-------|-------|---------|
| `core` | Blue | Fundamental concepts |
| `technique` | Green | Methods and approaches |
| `model` | Purple | Specific LLMs |
| `tool` | Orange | Software and frameworks |
| `paper` | Red | Research papers |

---

## 6. Auto-Deploy with GitHub Actions

The `.github/workflows/pages.yml` file in this repo automatically deploys to GitHub Pages on every push to `main`. No manual steps needed after the initial setup.

To verify it's working: push a change, then go to **Actions** tab in your GitHub repo — you'll see the deployment run.

---

## 7. Keeping the Wiki URL in Sync

Once live, update two places with your real GitHub username:

1. `README.md` — the badge link and graph link
2. `docs/index.html` — the "Back to GitHub" link in the header

Search for `your-username` across the repo to find all placeholders.

---

## Related Pages

- [What is an LLM Wiki?](what-is-llm-wiki.md)
- [Daily Workflow Integration](daily-workflow.md)
- [Concepts Map](concepts-map.md)

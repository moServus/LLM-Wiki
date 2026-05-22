# Publishing to GitHub

## Step 1 — Create a GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Name it `llm-wiki`
3. Visibility: **Public** (required for free GitHub Pages)
4. Do NOT check "Initialize this repository" — you already have files
5. Click **Create repository**

---

## Step 2 — Push Your Local Wiki

Open Terminal in the `LLM Wiki` folder and run:

```bash
git init
git add .
git commit -m "initial: LLM wiki with D3 concept graph"
git remote add origin https://github.com/YOUR_USERNAME/llm-wiki.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 3 — Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. Under **Source** → choose **GitHub Actions**
3. That's it — the workflow in `.github/workflows/pages.yml` handles the rest

Your site will be live at:
```
https://YOUR_USERNAME.github.io/llm-wiki
```

---

## Step 4 — Update Your Username Throughout

Search for `your-username` in these files and replace with your GitHub username:

| File | What to update |
|------|---------------|
| `README.md` | Badge URL and graph link |
| `docs/index.html` | GitHub link in the header |
| `docs/_config.yml` | `url:` field |

Then commit and push:
```bash
git add .
git commit -m "config: update GitHub username"
git push
```

---

## Step 5 — Adding New Wiki Pages

1. Create a new `.md` file in `wiki/`
2. Open `docs/graph-data.js` and add a node + links (see the existing entries for examples)
3. Commit and push — GitHub Pages will redeploy automatically in ~30 seconds

```bash
git add .
git commit -m "add: wiki page for <concept>"
git push
```

---

## Local Preview

To preview the graph before pushing:

```bash
# Open the graph directly in your browser
open docs/index.html
```

No server needed — the graph is pure client-side HTML/JS.

---

## Troubleshooting

**Graph not loading?**
- Make sure `docs/graph-data.js` is in the same folder as `docs/index.html`
- Check the browser console for JavaScript errors (Cmd+Option+I on Mac)

**GitHub Pages not updating?**
- Go to your repo → Actions tab — look for the "Deploy to GitHub Pages" workflow
- If it's failing, check the error log there

**`404` on GitHub Pages?**
- Make sure the source is set to **GitHub Actions** (not a branch/folder)
- Wait ~1 min after first push for the site to spin up

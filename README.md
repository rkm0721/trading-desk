# The Trading Desk

A personal trading-insights blog, written and published entirely from your phone.

## How you'll actually use this (weekly workflow)

1. **You give the input.** After a trading session, jot rough notes in Claude
   app or Termux — e.g. "Sat out today's rally, RSI overbought on Nifty,
   waiting for pullback to 22200, watching FII data tomorrow."

2. **AI drafts the article.** Ask Claude: *"Turn these trading notes into a
   short blog article with a title, a 'the setup' section, and a 'what I'm
   watching' section."* Claude writes the article text for you.

3. **You paste it into the site.** Copy `articles/first-entry.html`, rename
   it (e.g. `articles/2026-08-21-sitting-out-rally.html`), replace the title
   and paragraphs with what Claude drafted.

4. **Add it to the homepage.** Open `index.html`, copy one `<a class="entry">`
   block, update the link, date, title, and one-line excerpt.

5. **Push to GitHub — live in under a minute.**
   ```bash
   cd ~/trading-site
   git add .
   git commit -m "New entry: Sitting out the rally"
   git push
   ```

Your site updates automatically at your GitHub Pages URL a few seconds after
pushing.

## First-time setup (do this once)

```bash
cd ~/trading-site
git init
git add .
git commit -m "Initial site"
```

Create an empty repo on GitHub named e.g. `trading-desk`, then:
```bash
git remote add origin https://github.com/YOUR_USERNAME/trading-desk.git
git branch -M main
git push -u origin main
```

**Turn on GitHub Pages:**
- Go to your repo on GitHub → **Settings** → **Pages**
- Under "Branch," select `main` and folder `/ (root)` → Save
- Your live URL appears in a minute or two:
  `https://YOUR_USERNAME.github.io/trading-desk/`

## Files

- `index.html` — homepage, lists all entries
- `articles/first-entry.html` — sample article, use as your template
- `style.css` — the terminal-inspired look, no need to touch this

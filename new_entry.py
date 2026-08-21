#!/usr/bin/env python3
"""
new_entry.py — Interactive trading journal entry generator.

Run this from inside your trading-site folder:
    python new_entry.py

It asks a few quick questions, then:
1. Creates a new article HTML file in articles/
2. Adds a linked entry card to the top of index.html

After running, just review the file, then:
    git add .
    git commit -m "New entry: <title>"
    git push
"""

import re
import datetime
import os

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:60].strip("-")

def ask(prompt, default=""):
    val = input(f"{prompt}{' [' + default + ']' if default else ''}: ").strip()
    return val if val else default

def main():
    print("=== New Trading Journal Entry ===\n")

    today = datetime.date.today().strftime("%d %b %Y").upper()
    date_str = ask("Date", today)
    ticker = ask("Ticker (e.g. ES, NQ, CL)", "ES")
    title = ask("Title (e.g. 'Why I Passed on the NQ Breakout')")
    if not title:
        print("Title is required. Exiting.")
        return

    setup = ask("The setup — what happened / what you saw")
    risk = ask("Risk & account status — size, stop, drawdown used")
    watching = ask("What you're watching next")
    excerpt = ask("One-line excerpt for the homepage card", setup[:100])

    slug = slugify(title)
    filename = f"{datetime.date.today().isoformat()}-{slug}.html"
    filepath = os.path.join("articles", filename)

    if os.path.exists(filepath):
        print(f"File {filepath} already exists — aborting to avoid overwrite.")
        return

    article_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — The Trading Desk</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>

<div class="ticker-bar pressed">
  <div class="ticker-track">
    <span class="up">ES 5,612.25 &#9650; 0.4%</span>
    <span class="down">NQ 19,840.50 &#9660; 0.3%</span>
    <span class="up">CL 78.42 &#9650; 0.8%</span>
    <span>GC 2,415.10 &mdash;</span>
    <span class="down">RTY 2,201.80 &#9660; 0.1%</span>
    <span class="up">ES 5,612.25 &#9650; 0.4%</span>
    <span class="down">NQ 19,840.50 &#9660; 0.3%</span>
    <span class="up">CL 78.42 &#9650; 0.8%</span>
    <span>GC 2,415.10 &mdash;</span>
    <span class="down">RTY 2,201.80 &#9660; 0.1%</span>
  </div>
</div>

<main>
  <article class="post raised">
    <span class="post-meta">{date_str} &middot; EVAL NOTES &middot; {ticker}</span>
    <h1>{title}</h1>

    <h2>The setup</h2>
    <p>{setup}</p>

    <h2>Risk & account status</h2>
    <p>{risk}</p>

    <h2>What I'm watching next</h2>
    <p>{watching}</p>

    <a class="back-link pressed" href="../index.html">&larr; Back to all entries</a>
  </article>
</main>

<footer>
  Built and maintained from a phone. Updated whenever the market teaches something new.
</footer>

</body>
</html>
"""

    with open(filepath, "w") as f:
        f.write(article_html)

    # --- Insert entry card into index.html ---
    with open("index.html", "r") as f:
        index_content = f.read()

    entry_card = f'''  <a class="entry raised" href="articles/{filename}">
    <span class="entry-meta">{date_str} &middot; EVAL NOTES &middot; {ticker}</span>
    <h2 class="entry-title">{title}</h2>
    <p class="entry-excerpt">{excerpt}</p>
  </a>

'''

    marker = '<main id="entries">\n'
    if marker in index_content:
        index_content = index_content.replace(marker, marker + entry_card, 1)
        with open("index.html", "w") as f:
            f.write(index_content)
        print(f"\nAdded entry card to index.html")
    else:
        print("\nCouldn't find the insertion point in index.html — add the card manually.")
        print(entry_card)

    print(f"Created article: {filepath}")
    print("\nNext steps:")
    print("  git add .")
    print(f'  git commit -m "New entry: {title}"')
    print("  git push")

if __name__ == "__main__":
    main()

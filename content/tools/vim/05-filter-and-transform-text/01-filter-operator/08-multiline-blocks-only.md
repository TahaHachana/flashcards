## Filter Quirk — Multi-Line Blocks Only

Why does `!w` (filter a word) fail, and which motions are valid for filtering?

---

Filter blocks must span more than one line. Only motions that move across whole lines work — `G`, `{` `}`, `(` `)`, `[[` `]]`, `+`, `-` — so a single-line motion like `w` won't work unless enough are given to exceed one line.


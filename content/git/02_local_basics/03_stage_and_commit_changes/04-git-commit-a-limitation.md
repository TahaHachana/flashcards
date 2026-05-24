## git commit -a Limitation

You create a new file `feature.py` and also edit `README.md`. You run `git commit -a -m "Add feature"`. What gets committed?

---

Only the changes to **`README.md`** (an already-tracked file) are committed. The new file **`feature.py`** is **not committed** — it remains untracked.

`git commit -a` auto-stages modifications and deletions for files that Git already tracks, but it never stages brand-new untracked files. To include `feature.py` you must explicitly run `git add feature.py` first.


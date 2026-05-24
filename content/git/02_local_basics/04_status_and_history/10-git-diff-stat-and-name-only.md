## git diff --stat and --name-only

When would you use `git diff --stat` or `git diff --name-only` instead of a plain `git diff`?

---

```
git diff --stat    → Shows a summary: filename, a bar chart of
                     relative change size, and a count of
                     insertions/deletions per file.
                     Use when you want a quick overview of which
                     files changed and how much, without reading
                     every changed line.

   Example output:
   src/app.py | 12 ++++++------
   README.md  |  3 +++
   2 files changed, 15 insertions(+), 6 deletions(-)

git diff --name-only → Lists only the filenames that changed,
                       one per line, with no other output.
                       Use in scripts or when you just need the
                       list of affected paths.
```


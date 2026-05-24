## --stat vs -p in git log

What output does `--stat` add to `git log`, and how does it differ from `-p`?

---

```
--stat   → Appends a file-level summary after each commit:
           filenames, a proportional +/- bar, and net line counts.
           Good for a quick overview of what changed without
           reading every line.

           index.html | 5 ++++-
           1 file changed, 4 insertions(+), 1 deletion(-)

-p       → Appends the FULL unified diff (every changed line)
(--patch)  after each commit. Equivalent to running git show
           on each commit in sequence. Much more verbose but
           gives complete code-level detail.
```

Use `--stat` for a broad scan; use `-p` for deep code archaeology on a specific file or feature.


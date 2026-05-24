## The Empty Commit

By default, what does Git do if you try to commit with nothing staged, and how do you override this behaviour?

---

By default, Git **refuses** to create a commit with an empty staging area (nothing changed since the last commit) and prints:

```
nothing to commit, working tree clean
```

To force an empty commit (useful for triggering CI pipelines or adding documentation markers):

```bash
git commit --allow-empty -m "Trigger CI pipeline"
```

The resulting commit has no diff — it contains only metadata (message, author, timestamp, parent pointer).


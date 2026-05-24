## File States in the Working Directory

List the four states a file known to Git can be in within the working directory and explain each.

---

```
Untracked  → New file Git has never been told about.
              Exists on disk, invisible to Git history.

Clean      → Committed and identical to the HEAD version.
              No differences between disk and repository.

Modified   → Committed previously, but edited on disk since
              the last commit. Git sees a difference.

Deleted    → Was committed, but the file has been removed
              from disk. Git sees it as a pending deletion.
```

A fifth category — **Ignored** — applies to files matched by `.gitignore`; Git treats them as if they do not exist.


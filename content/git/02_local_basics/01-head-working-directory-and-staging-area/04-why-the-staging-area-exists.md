## Why the Staging Area Exists

What would be lost if Git had no staging area and committed the entire working directory directly?

---

Without a staging area every commit would capture **all** modified files at once, making it impossible to:

- **Separate concerns** — group only the files relevant to one logical change into a single commit while leaving unrelated edits aside.
- **Stage partial file changes** — use `git add -p` to commit individual hunks within a file, keeping different fixes in different commits.
- **Review before committing** — use `git diff --staged` to inspect exactly what will be recorded, catching mistakes before they enter history permanently.

The staging area transforms commits from "whatever happened to be modified" into deliberately crafted, meaningful snapshots.


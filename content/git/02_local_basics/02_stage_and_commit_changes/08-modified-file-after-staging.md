## Modified File After Staging

What happens if you stage a file with `git add`, then modify it again before committing?

---

The file appears in BOTH "Changes to be committed" and "Changes not staged for commit" in `git status`.

The staged version has the first edit, the working directory has the second edit. You must run `git add` again to stage the latest changes. Git stages the file's state at the moment you run `git add`, not continuously.


## What git init Creates

What does `git init` create, where does it create it, and does it affect existing files in the directory?

---

`git init` creates a hidden **`.git/`** subdirectory inside the target directory. This subdirectory is the repository — it holds all of Git's data (object database, branch refs, configuration, hooks). Existing files in the directory are **not touched, staged, or committed**; they simply become eligible to be tracked once you explicitly run `git add`.


## git show vs git log

What is the fundamental difference between `git log` and `git show`?

---

```
git log    → Lists MANY commits (metadata only by default).
             Used to navigate history and find a commit of
             interest. No diff shown unless -p is added.

git show   → Focuses on ONE commit: shows full metadata
             PLUS the unified diff that commit introduced.
             Used to inspect what a specific commit changed.
```

`git show` without arguments always shows the **HEAD** commit. Pass any ref, hash, branch name, or tag to show any other commit:
```bash
git show HEAD~3
git show v2.1.0
git show feature-branch
```


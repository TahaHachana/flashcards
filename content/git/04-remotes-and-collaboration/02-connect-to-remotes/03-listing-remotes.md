## Listing Remotes

How do you list remotes and view their URLs?

---

List remote names:
```bash
git remote
# origin
```

List with URLs (verbose):
```bash
git remote -v
# origin  https://github.com/user/project.git (fetch)
# origin  https://github.com/user/project.git (push)
```

Two lines per remote:
- (fetch): URL for pulling/fetching
- (push): URL for pushing

Usually the same, but can differ for specialized setups.


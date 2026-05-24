## Where the Index Is Stored

Where is the staging area physically stored, and which commands directly modify it?

---

The staging area is stored in the binary file **`.git/index`** at the root of the repository. You never edit it directly. The commands that modify it are:

```
git add <file>              → add/update file snapshot in index
git add -p                  → interactively stage hunks
git rm --cached <file>      → remove file from index (keep on disk)
git reset HEAD <file>       → restore index entry to HEAD version
git restore --staged <file> → same as above (modern syntax)
git commit                  → reads index, writes commit, clears
                              it to match the new HEAD
```


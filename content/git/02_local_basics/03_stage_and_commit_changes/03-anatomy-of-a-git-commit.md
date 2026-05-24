## Anatomy of a Git Commit

List the six fields stored inside every Git commit object.

---

```
1. SHA-1 hash    40-character unique identifier derived from all
                 content in the commit.

2. Tree          Pointer to a tree object — a full snapshot of
                 all tracked files and directories.

3. Parent(s)     SHA-1 of the preceding commit(s). None for the
                 root commit; two for a merge commit.

4. Author        Name, email, and timestamp of who wrote the change.

5. Committer     Name, email, and timestamp of who recorded the
                 commit (may differ from author in patch workflows).

6. Message       Human-readable description of the change.
```


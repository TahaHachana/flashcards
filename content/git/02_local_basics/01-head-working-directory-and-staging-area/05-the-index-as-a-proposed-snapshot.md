## The Index as a Proposed Snapshot

Why is it more accurate to think of the staging area as a "proposed next snapshot" rather than a "list of changes"?

---

The staging area holds a **complete snapshot of every tracked file** as you intend it to be at the time of the next commit — not just a diff or a queue of changes. When you run `git add file.txt`, you are updating the full-project snapshot stored in the index to include the current version of `file.txt`. When you commit, the entire index snapshot is written as a new commit object. This is why:

- Reverting a staged file (`git restore --staged file.txt`) restores it to the HEAD version, not to some intermediate "un-staged" state.
- Two `git add` calls on the same file overwrite the first — only the latest version enters the snapshot.


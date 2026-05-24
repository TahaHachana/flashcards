## What Happens Internally During git commit

Describe the internal sequence of steps Git takes when you run `git commit -m "message"`.

---

1. Git reads the current staging area (index).
2. Creates **blob** objects in `.git/objects/` for any file content not already stored.
3. Creates **tree** objects representing each directory's file listing.
4. Creates the **commit** object containing: the root tree SHA-1, parent commit SHA-1(s), author/committer metadata, and the message.
5. Updates the current **branch ref** (e.g., `refs/heads/main`) to point to the new commit's SHA-1.
6. HEAD, which points to the branch, now implicitly resolves to the new commit.


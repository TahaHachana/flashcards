## Crash Recovery — Swap Files in Vim

How does Vim protect work in progress against a system crash, and how do you recover?

---

Vim continuously writes edits to a swap file in the same directory as the file being edited. For a file named `practice`, the swap file is `.practice.swp`.

After a crash, the next time you open the same file, Vim detects the swap file and offers to recover. To recover:
1. Accept the recovery prompt (or run `vim -r practice`).
2. Immediately write the recovered buffer (`:w`).
3. Quit and manually delete the `.practice.swp` file.
4. Re-open the file to continue editing normally.


## --all Flag Scope

Why does `git log` without `--all` sometimes show far fewer commits than expected, and what does `--all` change?

---

Without `--all`, `git log` shows only commits **reachable from the current HEAD** — i.e., the history of the checked-out branch. Commits that exist on other branches are completely hidden.

`--all` instructs Git to include commits reachable from **every ref** in the repository:
- All local branches
- All remote-tracking branches (e.g., `origin/feature`)
- All tags

This is why `--all` is always paired with `--graph` for a full picture of the repository's parallel histories.


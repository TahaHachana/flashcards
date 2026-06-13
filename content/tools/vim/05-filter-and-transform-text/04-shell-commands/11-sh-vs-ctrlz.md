## sh Versus CTRL-Z

What is the difference between `:sh` and `CTRL-Z`?

---

`:sh` starts a NEW subshell as a child of Vim (return with CTRL-D); `CTRL-Z` SUSPENDS the existing Vim process back to its parent shell (return with `fg`).


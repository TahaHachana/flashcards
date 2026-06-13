## Registers Across Files

Are named registers cleared when you load a new file with `:e`?

---

No. Named registers persist across `:e`, so you can yank text, switch files, and put it into the new file. They're shared across windows in one session but not between separate Vim sessions.


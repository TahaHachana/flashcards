## autowrite And Shelling Out

If the `autowrite` option is set, what happens before Vim runs a `:!` shell command?

---

Vim automatically writes out the changed buffer (it also does this before `:n` to move to the next file), protecting unsaved work.


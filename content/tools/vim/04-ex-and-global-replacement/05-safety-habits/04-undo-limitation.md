## Limitation Of Undo

What is the key limitation of `u` for recovering from a bad substitution?

---

`u` reverses a search-and-replace only if it was the most recent edit. If you made changes since then or didn't notice immediately, `u` can't help — but `:e!` (revert to last save) can.


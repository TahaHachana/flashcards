## Named Register Lifespan

Why use a named register (`a`–`z`) instead of relying on the unnamed register?

---

Named registers keep their contents for the whole editing session, so they survive intervening edits — whereas the unnamed register is overwritten by the next delete or yank.


# Packfiles and Their Purpose

What are packfiles and why are they used?

---

Packfiles (`.git/objects/pack/*.pack`) compress many objects into one file plus an index (`.idx`) for efficient storage and network transfer.

List existing packfiles with:

```bash
ls .git/objects/pack
```

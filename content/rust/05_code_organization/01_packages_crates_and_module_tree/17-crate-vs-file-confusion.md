## Crate vs File Confusion

Why is it wrong to think "one file = one crate"?

---

**Wrong assumption:** Each `.rs` file is a separate crate.

**Reality:**
- A crate is a tree of modules, potentially spanning many files
- The compiler compiles entire crates, not individual files
- All files that are part of the module tree are compiled together as one crate

**Example:** A library crate can have:
- `src/lib.rs` (root)
- `src/database.rs` (module)
- `src/api.rs` (module)
- `src/models.rs` (module)

These are all part of ONE crate.


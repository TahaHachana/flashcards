## Crate as Compilation Unit

Why is the crate considered the "compilation unit" in Rust, and what does this mean?

---

A crate is the **smallest amount of code the Rust compiler considers at a time**.

**What this means:**
- The compiler analyzes an entire crate at once, not individual files
- All files in a crate are compiled together
- The borrow checker operates within crate boundaries
- Compilation happens at the crate level, not the file level

**Implication:** Even if your crate spans multiple files, they're all compiled as a single unit.


## Connection Between Crates and Compilation

How do crates relate to Rust's compilation process and the borrow checker?

---

**Compilation:**
- Crates are compiled independently (one at a time)
- The compiler analyzes an entire crate together
- Each crate is a separate compilation unit

**Borrow checker:**
- Operates within crate boundaries
- When you use external crates, their ownership rules are already validated
- You don't re-check external crate internals

**Implication:** 
- Crate boundaries provide compilation isolation
- Changes in one crate don't require recompiling unaffected crates
- The borrow checker works on a per-crate basis


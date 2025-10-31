## Rust's Privacy Philosophy

What is Rust's core privacy philosophy, and why does it matter?

---

**Philosophy**: Rust is **private by default**. Everything starts as private, and you must explicitly make things public using `pub`.

**Why it matters**:
- Encourages good API design
- Prevents accidental exposure of internal details
- Forces deliberate decisions about what's public
- Makes it safe to change private implementation without breaking external code

**Exceptions**: Items in a `pub` trait and variants in a `pub` enum are automatically public.


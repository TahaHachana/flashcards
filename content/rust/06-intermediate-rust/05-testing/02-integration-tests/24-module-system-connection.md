## Module System Connection

How do integration tests reinforce understanding of Rust's module system?

---

Integration tests demonstrate module visibility rules:

```rust
// src/lib.rs
pub fn public() {}              // ✅ Visible in integration tests
pub(crate) fn crate_only() {}   // ❌ Not visible (crate-private)
fn private() {}                 // ❌ Not visible

pub mod public_mod {
    pub fn accessible() {}       // ✅ Visible (module and fn public)
    fn hidden() {}               // ❌ Not visible (fn private)
}

mod private_mod {
    pub fn looks_public() {}     // ❌ Not visible (module private)
}
```

Integration tests show:
- What "public" truly means
- How `pub(crate)` differs from `pub`
- Module boundary enforcement
- Real-world API visibility

This helps understand Rust's privacy system from external perspective.


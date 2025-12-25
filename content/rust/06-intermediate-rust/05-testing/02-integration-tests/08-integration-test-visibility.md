## What Can Be Accessed in Integration Tests

What items from your library can integration tests access?

---

Integration tests can only access:
- Items marked `pub` in `src/lib.rs`
- Items re-exported from `src/lib.rs`
- Public items in public modules

```rust
// src/lib.rs
pub fn accessible() {}      // ✅ Can test
fn not_accessible() {}      // ❌ Cannot test

pub mod public_module {
    pub fn also_accessible() {}  // ✅ Can test
    fn hidden() {}               // ❌ Cannot test
}

mod private_module {
    pub fn looks_public() {}     // ❌ Cannot test (module private)
}

pub(crate) fn crate_only() {}    // ❌ Cannot test (crate-private)
```

This enforces testing through your public API only.


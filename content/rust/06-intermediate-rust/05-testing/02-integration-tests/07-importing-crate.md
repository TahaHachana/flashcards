## Importing Crate in Tests

How do integration tests import the crate being tested?

---

Import using the crate name from `Cargo.toml`:

**Cargo.toml:**
```toml
[package]
name = "awesome_lib"
```

**Integration test:**
```rust
// tests/my_test.rs
use awesome_lib;  // Use exact name from Cargo.toml

#[test]
fn test() {
    awesome_lib::public_function();
}
```

Common mistake:
```rust
use my_project;  // ❌ Wrong if Cargo.toml says "awesome_lib"
```

The crate name must match exactly.


## Wrong Crate Name Error

What happens if you use the wrong crate name in integration tests?

---

Error occurs when test uses different name than Cargo.toml:

**Cargo.toml:**
```toml
[package]
name = "my_awesome_lib"
```

**Wrong:**
```rust
// tests/test.rs
use my_project;  // ❌ ERROR: No crate named 'my_project'

#[test]
fn test() {
    my_project::function();
}
```

**Correct:**
```rust
use my_awesome_lib;  // ✅ Matches Cargo.toml

#[test]
fn test() {
    my_awesome_lib::function();
}
```

Always check the `name` field in `Cargo.toml`.


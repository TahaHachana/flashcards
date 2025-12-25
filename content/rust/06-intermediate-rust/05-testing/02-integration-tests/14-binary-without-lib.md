## Binary Without lib.rs Problem

What happens when you try to write integration tests for a binary-only project?

---

Problem: No library to import:

```
my_binary/
├── Cargo.toml
├── src/
│   └── main.rs      # Only binary, no lib.rs
└── tests/
    └── test.rs      # ❌ Nothing to import!
```

```rust
// tests/test.rs
use my_binary;  // ❌ ERROR: Binary crates cannot be imported
```

Solution: Create library alongside binary:
```
my_project/
├── Cargo.toml
├── src/
│   ├── lib.rs       # ✅ Library with logic (testable)
│   └── main.rs      # ✅ Thin wrapper
└── tests/
    └── test.rs      # ✅ Can test lib.rs
```

This is the idiomatic Rust approach for testable binaries.


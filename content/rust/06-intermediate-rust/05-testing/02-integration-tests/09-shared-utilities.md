## Shared Test Utilities Pattern

How do you share helper functions across multiple integration test files without creating extra test binaries?

---

Use subdirectories (not files) for shared utilities:

**Wrong (creates extra test binary):**
```
tests/
├── common.rs        # ❌ Becomes test binary with 0 tests
└── my_test.rs
```

**Correct (subdirectory not compiled as test):**
```
tests/
├── common/          # ✅ Subdirectory (not a test binary)
│   └── mod.rs       # Shared utilities
└── my_test.rs       # Actual test file
```

**tests/common/mod.rs:**
```rust
pub fn setup() -> TestContext { /* ... */ }
```

**tests/my_test.rs:**
```rust
mod common;  // Import shared utilities

#[test]
fn test() {
    let ctx = common::setup();
}
```

Key: Cargo treats subdirectories differently from files.


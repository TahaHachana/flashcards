## Doc Comment Syntax /// vs //!

What's the difference between `///` and `//!` in documentation comments?

---

`///` documents the **next item**:
```rust
/// Adds two numbers.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

`//!` documents the **containing item** (module/crate):
```rust
//! This module provides math utilities.

pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Usage:
- `///` for functions, structs, methods, fields
- `//!` for module-level or crate-level docs
- Both can contain code examples in triple backticks

Triple slashes for items, exclamation for containers.


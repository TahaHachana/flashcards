## Module-Level Documentation

How do you write module-level documentation?

---

Use //! (with exclamation mark) at the top of the file.

```rust
//! This module provides math utilities.
//!
//! It includes basic arithmetic functions.

pub fn add(a: i32, b: i32) -> i32 { a + b }
```


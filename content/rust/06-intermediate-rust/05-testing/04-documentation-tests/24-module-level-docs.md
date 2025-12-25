## Doc Test Module Level Documentation

How do you write module-level documentation with examples?

---

Use `//!` at the top of the module:

```rust
//! Mathematical utility functions.
//!
//! This module provides basic arithmetic operations
//! with proper error handling.
//!
//! # Examples
//!
//! ```
//! use my_crate::math;
//!
//! let sum = math::add(2, 3);
//! assert_eq!(sum, 5);
//!
//! let product = math::multiply(4, 5);
//! assert_eq!(product, 20);
//! ```

pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

pub fn multiply(a: i32, b: i32) -> i32 {
    a * b
}
```

Module docs should:
- Explain module purpose
- Show typical usage
- Demonstrate how items work together
- Provide complete working examples

Use `//!` for the container, `///` for items.


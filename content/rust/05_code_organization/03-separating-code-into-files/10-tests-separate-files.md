## Tests in Separate Files

How do you organize tests in separate files, and why can they still access private items?

---

**Organization**:
```rust
// src/calculator.rs
pub fn add(a: i32, b: i32) -> i32 { a + b }

#[cfg(test)]
mod tests;

// src/calculator/tests.rs
use super::*;

#[test]
fn test_add() {
    assert_eq!(add(2, 2), 4);
}
```

**Why tests can access private items**:
- The test module is a **child module** of the code it tests
- Child modules can access parent items regardless of visibility
- `#[cfg(test)]` only compiles the tests during `cargo test`

**Benefits**:
- Keeps test code separate from implementation
- Main source files stay cleaner
- Tests still have full access to private functions


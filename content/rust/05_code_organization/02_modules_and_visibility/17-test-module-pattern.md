## Test Module Pattern

How do you organize tests to keep them close to the code they test, and why can they access private items?

---

**Pattern**:
```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn internal_helper() -> i32 {  // Private function
    42
}

#[cfg(test)]
mod tests {
    use super::*;  // Import from parent module
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }
    
    #[test]
    fn test_helper() {
        assert_eq!(internal_helper(), 42);  // Can test private!
    }
}
```

**Why tests can access private items**: The test module is a child of the module it tests, and child modules can access parent items regardless of visibility.

**`#[cfg(test)]`**: Only compiles this module during `cargo test`.


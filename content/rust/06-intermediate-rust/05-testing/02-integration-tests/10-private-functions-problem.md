## Testing Private Functions Problem

Why can't integration tests access private functions, and what's the solution?

---

Problem:
```rust
// src/lib.rs
fn internal_helper() -> i32 { 42 }

pub fn public_function() -> i32 {
    internal_helper()
}
```

```rust
// tests/test.rs
#[test]
fn broken() {
    // ❌ ERROR: internal_helper is not public
    let result = my_project::internal_helper();
}
```

Solutions:

1. Test through public API:
```rust
#[test]
fn correct() {
    let result = my_project::public_function();
    assert_eq!(result, 42);
}
```

2. Use unit tests in source file for private functions:
```rust
// src/lib.rs
#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_internal() {
        assert_eq!(internal_helper(), 42);
    }
}
```


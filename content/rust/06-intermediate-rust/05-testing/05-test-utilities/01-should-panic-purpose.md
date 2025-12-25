## #[should_panic] Attribute Purpose

What does `#[should_panic]` do and when should you use it?

---

`#[should_panic]` marks tests that expect code to panic:

```rust
#[test]
#[should_panic]
fn test_divide_by_zero() {
    divide(10, 0);  // Should panic
}
```

Test behavior:
- ✅ Passes if code panics
- ❌ Fails if code doesn't panic

Use for:
- Input validation errors
- Precondition violations
- Invalid state transitions
- Boundary condition failures

Example:
```rust
pub fn divide(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Cannot divide by zero");
    }
    a / b
}

#[test]
#[should_panic]
fn test_panic_on_zero() {
    divide(10, 0);
}
```

Essential for testing that code fails correctly in invalid scenarios.


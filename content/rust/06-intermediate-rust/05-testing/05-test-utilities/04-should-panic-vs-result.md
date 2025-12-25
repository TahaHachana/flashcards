## #[should_panic] vs Result

What's the difference between testing panics with `#[should_panic]` versus testing Result errors?

---

Different error handling approaches need different tests:

**Function that panics:**
```rust
pub fn divide(a: i32, b: i32) -> i32 {
    if b == 0 { panic!("Cannot divide by zero"); }
    a / b
}

#[test]
#[should_panic(expected = "divide by zero")]
fn test_panic() {
    divide(10, 0);  // ✅ Correct: expects panic
}
```

**Function that returns Result:**
```rust
pub fn safe_divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 { return Err("Cannot divide by zero".to_string()); }
    Ok(a / b)
}

#[test]
fn test_error() {
    let result = safe_divide(10, 0);
    assert!(result.is_err());  // ✅ Correct: tests Result
}

#[test]
#[should_panic]  // ❌ Wrong: doesn't panic, returns Err
fn test_panic() {
    safe_divide(10, 0);
}
```

Use `#[should_panic]` for panics, `assert!(result.is_err())` for Result errors.


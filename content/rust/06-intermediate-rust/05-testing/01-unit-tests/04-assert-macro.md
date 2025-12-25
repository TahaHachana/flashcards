## The assert! Macro

What does `assert!(condition)` do and when should you use it?

---

`assert!(condition)` panics if the boolean condition is `false`.

Use when testing boolean expressions:
```rust
#[test]
fn test_validation() {
    let is_valid = true;
    assert!(is_valid);
    
    let count = 5;
    assert!(count > 0);
    assert!(count < 10);
}
```

With custom message:
```rust
assert!(age >= 18, "User must be 18+, got: {}", age);
```

When it fails, shows: `assertion failed: age >= 18`


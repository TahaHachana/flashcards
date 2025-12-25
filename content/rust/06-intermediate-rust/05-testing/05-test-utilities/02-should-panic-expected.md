## #[should_panic] Expected Message

How does the `expected` parameter work with `#[should_panic]`?

---

The `expected` parameter verifies panic message content:

```rust
pub fn validate_age(age: i32) {
    if age < 0 {
        panic!("Age cannot be negative");
    }
    if age > 150 {
        panic!("Age cannot exceed 150");
    }
}

#[test]
#[should_panic(expected = "cannot be negative")]
fn test_negative_age() {
    validate_age(-5);  // ✅ Passes: message contains substring
}

#[test]
#[should_panic(expected = "must be positive")]
fn test_wrong_message() {
    validate_age(-5);  // ❌ Fails: message doesn't contain substring
}
```

Behavior:
- Checks if panic message **contains** expected string
- Case-sensitive substring match
- Test fails if:
  - Code doesn't panic
  - Panic message doesn't contain expected string

Prevents false positives from panics in wrong places.


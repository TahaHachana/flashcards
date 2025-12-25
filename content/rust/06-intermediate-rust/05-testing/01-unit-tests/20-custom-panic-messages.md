## Custom Panic Messages

How do you add custom error messages to assert macros and why would you?

---

Add messages as additional arguments after the assertion:

```rust
assert!(condition, "format string", args...);
assert_eq!(left, right, "format string", args...);
assert_ne!(left, right, "format string", args...);
```

Example:
```rust
#[test]
fn test_age() {
    let age = 15;
    assert!(
        age >= 18,
        "User must be 18+, but got: {}",
        age
    );
}
```

Output:
```
panicked at src/lib.rs:4:5:
User must be 18+, but got: 15
```

Why: Provides context about what was being tested and why it matters, making failures easier to understand.


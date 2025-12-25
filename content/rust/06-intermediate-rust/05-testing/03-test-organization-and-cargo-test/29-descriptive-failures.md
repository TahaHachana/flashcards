## Descriptive Failure Messages

How should you write descriptive failure messages in tests?

---

Include context about what was tested and why it failed:

Basic:
```rust
#[test]
fn test_age() {
    let user = User::new("Alice", 15);
    assert!(user.age() >= 18);  // Not very helpful
}
```

With message:
```rust
#[test]
fn test_age() {
    let user = User::new("Alice", 15);
    assert!(
        user.age() >= 18,
        "Expected user {} to be adult (>=18), but age is {}",
        user.name(),
        user.age()
    );
}
```

Output when fails:
```
assertion failed: user.age() >= 18
Expected user Alice to be adult (>=18), but age is 15
```

Include:
- What was being tested
- Expected value
- Actual value
- Why it matters

Makes debugging much faster!


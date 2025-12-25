## #[should_panic] Common Patterns

What are common use cases for `#[should_panic]` tests?

---

1. **Input Validation:**
```rust
#[test]
#[should_panic(expected = "Name cannot be empty")]
fn test_empty_name() {
    create_user("", 25);
}
```

2. **Precondition Violations:**
```rust
#[test]
#[should_panic(expected = "empty stack")]
fn test_pop_empty() {
    let mut stack = Stack::new();
    stack.pop();  // Violates precondition
}
```

3. **Invalid State Transitions:**
```rust
#[test]
#[should_panic(expected = "not connected")]
fn test_send_disconnected() {
    let conn = Connection { connected: false };
    conn.send("data");  // Invalid state
}
```

4. **Invariant Violations:**
```rust
#[test]
#[should_panic(expected = "Total cannot be zero")]
fn test_zero_total() {
    calculate_percentage(50.0, 0.0);
}
```

Test that code enforces contracts correctly.


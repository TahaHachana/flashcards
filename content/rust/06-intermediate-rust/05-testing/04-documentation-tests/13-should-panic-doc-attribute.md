## Doc Test should_panic Attribute

How do you document examples that are expected to panic in doc tests?

---

Use `should_panic` attribute:

```rust
/// Divides two numbers.
///
/// # Examples
///
/// Normal division:
/// ```
/// let result = divide(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// Division by zero panics:
/// ```should_panic
/// // This panics!
/// divide(10, 0);
/// ```
pub fn divide(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Cannot divide by zero");
    }
    a / b
}
```

Benefits:
- Shows users what causes panics
- Tests that panic behavior works
- Documents error conditions
- Verifies panic happens as expected

Use to demonstrate and verify panic conditions.


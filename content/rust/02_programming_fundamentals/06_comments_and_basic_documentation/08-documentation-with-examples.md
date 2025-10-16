## Documentation with Examples

How do you include code examples in documentation?

---

Use code blocks in doc comments. They're automatically tested by cargo test.

```rust
/// # Examples
/// ```
/// let result = add(2, 3);
/// assert_eq!(result, 5);
/// ```
fn add(a: i32, b: i32) -> i32 { a + b }
```


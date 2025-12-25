## Doc Test compile_fail Attribute

When should you use `compile_fail` in documentation tests?

---

Use `compile_fail` to show what **doesn't** compile:

```rust
/// This function requires a valid type.
///
/// # Examples
///
/// This works:
/// ```
/// let result = process(42);
/// assert_eq!(result, 84);
/// ```
///
/// This won't compile:
/// ```compile_fail
/// let result = process("not a number");  // Type error!
/// ```
pub fn process(x: i32) -> i32 {
    x * 2
}
```

Use for:
- Showing common mistakes
- Demonstrating type safety
- Explaining compiler errors
- Anti-patterns (what NOT to do)

Test passes if compilation fails, ensuring the anti-example stays invalid.

Great for teaching proper API usage by showing what fails.


## Code Examples in Doc Comments

How do you write code examples in documentation that become tests?

---

Use triple backticks in doc comments:

```rust
/// Multiplies two numbers.
///
/// # Examples
///
/// ```
/// let result = my_crate::multiply(3, 4);
/// assert_eq!(result, 12);
/// ```
pub fn multiply(a: i32, b: i32) -> i32 {
    a * b
}
```

When `cargo test` runs:
1. Extracts code from ` ``` ` blocks
2. Wraps in test function
3. Compiles and runs
4. Test passes if no panic

Output shows: `test src/lib.rs - multiply (line 5) ... ok`

Code automatically has access to your crate.


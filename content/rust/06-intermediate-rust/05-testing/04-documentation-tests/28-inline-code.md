## Doc Test Inline Code

How do you format inline code vs code blocks in documentation?

---

Use backticks for inline code:

```rust
/// Adds two numbers together.
///
/// The function takes two parameters: `a` and `b`,
/// both of type `i32`. It returns their sum as an `i32`.
///
/// Use `add(2, 3)` for simple addition, or see
/// [`add_many`] for adding multiple values.
///
/// # Examples
///
/// ```
/// let result = add(5, 7);
/// assert_eq!(result, 12);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Formatting:
- Single backticks: \`code\` for inline
- Triple backticks: \`\`\` for blocks
- Inline for: variable names, types, function names, keywords
- Blocks for: complete examples

Good inline code makes documentation scannable.


## Doc Test Link References

How do you create links to other items in documentation?

---

Use square brackets for auto-linking:

```rust
/// Processes data using the specified [`Config`].
///
/// See also [`validate`] for input validation.
///
/// # Examples
///
/// ```
/// use my_crate::{process, Config};
///
/// let config = Config::default();
/// let result = process("input", &config);
/// ```
///
/// For advanced usage, see [`Config::builder`].
pub fn process(input: &str, config: &Config) -> String {
    // Implementation
}

/// Validates input before processing.
///
/// Used internally by [`process`].
pub fn validate(input: &str) -> bool {
    !input.is_empty()
}
```

Linking:
- `[`Type`]` - Links to type
- `[`function`]` - Links to function
- `[`module::item`]` - Full path

Creates clickable links in rendered documentation.


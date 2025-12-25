## Multiple Examples Pattern

How should you organize multiple examples in documentation?

---

Organize by scenario with descriptive text:

```rust
/// Parses a string into an integer.
///
/// # Examples
///
/// Basic usage:
/// ```
/// let num = parse("42");
/// assert_eq!(num, Some(42));
/// ```
///
/// Invalid input returns None:
/// ```
/// let num = parse("abc");
/// assert_eq!(num, None);
/// ```
///
/// Handles negative numbers:
/// ```
/// let num = parse("-10");
/// assert_eq!(num, Some(-10));
/// ```
///
/// Empty string:
/// ```
/// let num = parse("");
/// assert_eq!(num, None);
/// ```
pub fn parse(s: &str) -> Option<i32> {
    s.parse().ok()
}
```

Benefits: Shows multiple use cases, covers edge cases, clear documentation.


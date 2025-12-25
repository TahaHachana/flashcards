## Doc Test Text Blocks

How do you include non-code text blocks in documentation?

---

Use triple backticks with `text` (or no language):

```rust
/// Parses configuration files.
///
/// Supported format:
/// ```text
/// key = value
/// another_key = another_value
/// [section]
/// nested_key = nested_value
/// ```
///
/// # Examples
///
/// ```
/// let config = parse_config("key = value\nfoo = bar");
/// assert_eq!(config.get("key"), Some("value"));
/// ```
```

Use `text` for:
- Configuration examples
- File format examples
- Command line examples
- Output examples

These blocks are NOT run as tests.

Use ` ```text ` for illustrations, ` ``` ` (rust) for executable examples.


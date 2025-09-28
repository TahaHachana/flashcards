## Function Doc Template

What is a recommended template for documenting a Rust function?

---

A function doc usually includes:

* One-line summary.
* `# Parameters` list.
* `# Returns` description.
* Optional: `# Panics`, `# Errors`, `# Safety`.
* At least one `# Examples` code block.

```rust
/// Adds one to a number.
///
/// # Parameters
/// - `x`: the input integer.
///
/// # Returns
/// The input plus one.
///
/// # Examples
/// ```
/// assert_eq!(add_one(1), 2);
/// ```
```


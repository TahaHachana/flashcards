## Doc Test Error Patterns

How do you document and test functions that return Result in doc tests?

---

Use hidden main wrapper with Result return:

```rust
/// Reads a file and returns its contents.
///
/// # Examples
///
/// ```
/// # use std::error::Error;
/// # fn main() -> Result<(), Box<dyn Error>> {
/// let content = read_config("config.toml")?;
/// assert!(content.contains("version"));
/// # Ok(())
/// # }
/// ```
///
/// # Errors
///
/// Returns an error if the file doesn't exist:
/// ```
/// # use std::error::Error;
/// # fn main() -> Result<(), Box<dyn Error>> {
/// let result = read_config("nonexistent.toml");
/// assert!(result.is_err());
/// # Ok(())
/// # }
/// ```
pub fn read_config(path: &str) -> Result<String, std::io::Error> {
    std::fs::read_to_string(path)
}
```

The hidden `main() -> Result` wrapper allows using `?` operator naturally.


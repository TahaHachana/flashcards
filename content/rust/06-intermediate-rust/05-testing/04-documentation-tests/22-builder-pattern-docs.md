## Doc Test Builder Pattern Example

How do you document builder patterns effectively in doc tests?

---

Show complete builder chain:

```rust
/// Creates a new configuration.
///
/// # Examples
///
/// Basic usage:
/// ```
/// let config = Config::builder()
///     .host("localhost")
///     .port(8080)
///     .build();
///
/// assert_eq!(config.host(), "localhost");
/// assert_eq!(config.port(), 8080);
/// ```
///
/// With optional settings:
/// ```
/// let config = Config::builder()
///     .host("example.com")
///     .port(443)
///     .timeout(30)
///     .retries(3)
///     .build();
///
/// assert_eq!(config.timeout(), 30);
/// ```
pub struct Config { /* ... */ }
```

Benefits:
- Shows full builder chain
- Demonstrates method chaining
- Shows optional vs required methods
- Clear, readable examples

Builder patterns need complete examples to be useful.


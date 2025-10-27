## Option In Struct Fields

How do you use `Option<T>` for optional struct fields and what's a common pattern for accessing them?

---

Declare optional fields with `Option<T>`:

```rust
struct Config {
    port: u16,
    host: Option<String>,  // Optional field
}

impl Config {
    fn get_host(&self) -> &str {
        self.host.as_deref().unwrap_or("localhost")
    }
}
```

Common pattern: use `as_deref()` to convert `Option<String>` to `Option<&str>`, then provide a default with `unwrap_or()`.


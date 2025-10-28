## Fallible Initialization Pattern

How do you create constructors (initialization functions) that can fail?

---

Return `Result` from a constructor (typically `new` or `try_new`):

```rust
struct Config {
    port: u16,
    host: String,
}

impl Config {
    fn new(port: i32, host: String) -> Result<Self, String> {
        if port < 0 || port > 65535 {
            return Err(format!("Invalid port: {}", port));
        }
        if host.is_empty() {
            return Err("Host cannot be empty".into());
        }
        Ok(Config {
            port: port as u16,
            host,
        })
    }
}
```

Convention: `new()` for infallible, `try_new()` for fallible constructors.


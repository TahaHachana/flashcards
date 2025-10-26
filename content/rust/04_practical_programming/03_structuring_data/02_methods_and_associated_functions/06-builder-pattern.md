## Builder Pattern with Method Chaining

How do you implement the builder pattern with method chaining in Rust?

---

Consume `self` and return `Self` to enable chaining:

```rust
struct Config {
    host: String,
    port: u16,
    debug: bool,
}

impl Config {
    fn new() -> Self {
        Config {
            host: String::from("localhost"),
            port: 8080,
            debug: false,
        }
    }
    
    fn host(mut self, host: String) -> Self {
        self.host = host;
        self  // Return self for chaining
    }
    
    fn port(mut self, port: u16) -> Self {
        self.port = port;
        self
    }
}

// Usage - beautiful chaining
let config = Config::new()
    .host(String::from("example.com"))
    .port(3000);
```


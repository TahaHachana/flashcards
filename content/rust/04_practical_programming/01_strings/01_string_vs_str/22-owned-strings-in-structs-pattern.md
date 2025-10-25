## Owned Strings in Structs Pattern

Why do structs typically store String rather than &str, and how do you handle this in a constructor?

---

Structs store String to own their data - the struct's lifetime shouldn't depend on external string data:
```rust
struct Config {
    host: String,  // Owned data
    port: u16,
}

impl Config {
    fn new(host: &str, port: u16) -> Self {
        Config {
            host: host.to_string(),  // Convert &str to String
            port,
        }
    }
}
```
The constructor accepts &str for flexibility, then converts to String for ownership.


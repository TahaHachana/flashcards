## Default Trait Derivation

How does the `Default` trait work when derived, and what does it produce?

---

When derived, `Default` creates a value with default values for all fields (each field must implement `Default`):

```rust
#[derive(Debug, Default)]
struct Config {
    timeout: u32,    // Defaults to 0
    retries: u32,    // Defaults to 0
}

fn main() {
    let config = Config::default();
    println!("{:?}", config);  
    // Output: Config { timeout: 0, retries: 0 }
}
```

Numbers default to 0, booleans to `false`, `String` to empty string, etc.


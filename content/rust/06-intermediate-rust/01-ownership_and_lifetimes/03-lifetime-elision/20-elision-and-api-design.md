## Elision and API Design

How does understanding elision influence good API design in Rust?

---

Good API design often aligns with elision rules because functions that follow elision patterns are easier to use and understand. For example:
```rust
// Good: Follows elision naturally
impl Config {
    fn get_value(&self, key: &str) -> Option<&str>
}

// Less ergonomic: Requires explicit lifetimes
fn merge<'a>(x: &'a str, y: &'a str) -> &'a str
```
When possible, design APIs so their most common usage patterns work with elision.


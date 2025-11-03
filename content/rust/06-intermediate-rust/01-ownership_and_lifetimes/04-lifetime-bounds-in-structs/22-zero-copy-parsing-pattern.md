## Zero-Copy Parsing Pattern

How do structs with lifetimes enable zero-copy parsing?

---

By holding references to input data and returning slices, parsers can work without allocating:
```rust
struct JsonParser<'a> {
    input: &'a str,
}
// Methods return &'a str slices into input
```
This is more efficient than cloning:
```rust
// Less efficient - requires cloning
struct Parser {
    input: String,
}
```
Zero-copy avoids allocation by borrowing instead of owning.


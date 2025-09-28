## Documentation Comments

What are Rust documentation comments and how do they differ from normal comments?

---

Rust has two forms of documentation comments:

* `///` for documenting **items** (functions, structs, traits).
* `//!` for documenting the **enclosing scope** (module, crate).

They support Markdown and are rendered by `cargo doc`.

```rust
/// Adds one to a number.
fn add_one(x: i32) -> i32 { x + 1 }
```


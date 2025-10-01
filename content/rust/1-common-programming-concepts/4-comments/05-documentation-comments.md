## Documentation Comments

What special comment syntax does Rust provide for generating documentation?

---

Rust provides documentation comments:

* `///` → documents the item that follows (outer doc comment).
* `//!` → documents the enclosing item, like a module or crate (inner doc comment).

These integrate with `rustdoc` to generate API docs.

```rust
/// Adds one to the input value
fn add_one(x: i32) -> i32 {
    x + 1
}
```


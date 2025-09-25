## Lifetime Annotations in Functions

When do you need to add explicit lifetime annotations in function signatures?

---

When a function returns a reference tied to one of its input references, and Rust cannot infer the relationship.

Example:

```rust
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() > b.len() { a } else { b }
}
```


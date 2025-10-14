## Missing Parameter Types Error

Can Rust infer parameter types like it infers variable types?

---

No. Parameter types must be explicitly annotated.

```rust
fn greet(name) { }  // ❌ Error: must specify type
fn greet(name: &str) { }  // ✅ Correct
```


## Parameter Types

Must parameter types be declared in Rust functions?

---

Yes. Every parameter in a function must have its type explicitly declared.

```rust
fn add(x: i32, y: i32) -> i32 {
    x + y
}
```


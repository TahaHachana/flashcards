## If Let Basics

What does `if let` do in Rust?

---

`if let` checks if a value matches a pattern and runs the block if it does:

```rust
let opt = Some(5);

if let Some(x) = opt {
    println!("Value = {x}");
}
```


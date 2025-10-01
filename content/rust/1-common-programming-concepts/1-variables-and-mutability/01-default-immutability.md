## Default Immutability

What is the default mutability of variables in Rust, and why?

---

By default, variables in Rust are **immutable**.  
This prevents accidental changes, improves safety, and makes reasoning about concurrent code easier.

```rust
fn main() {
    let x = 5;
    // x = 6; // ❌ compile-time error
    println!("x = {x}");
}
```


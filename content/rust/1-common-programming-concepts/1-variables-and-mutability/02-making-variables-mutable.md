## Making Variables Mutable

How do you make a variable mutable in Rust?

---

Add the `mut` keyword before the variable name when declaring it.

```rust
fn main() {
    let mut x = 5;
    println!("x = {x}");
    x = 6; // ✅ allowed
    println!("x = {x}");
}
```


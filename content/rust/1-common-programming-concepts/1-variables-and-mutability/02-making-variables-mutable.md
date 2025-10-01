## Making Variables Mutable

How do you declare a variable that can change value in Rust?

---

Add the `mut` keyword to the binding:

```rust
fn main() {
    let mut x = 5;
    println!("x = {x}");
    x = 6; // ✅ allowed
    println!("x = {x}");
}
```


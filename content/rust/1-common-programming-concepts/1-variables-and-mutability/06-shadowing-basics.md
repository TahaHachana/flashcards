## Shadowing Basics

What does it mean to shadow a variable in Rust?

---

Shadowing is when a new variable with the same name replaces the previous one.
The new binding is distinct from the old one.

```rust
fn main() {
    let x = 5;
    let x = x + 1; // shadows previous x
    println!("x = {x}"); // prints 6
}
```


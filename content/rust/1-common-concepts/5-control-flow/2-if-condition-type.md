# If Condition Type

What must the condition in an `if` expression evaluate to in Rust?

---

A `bool`. Rust does not automatically convert non-Boolean values.

```rust
fn main() {
    let number = 3;
    if number != 0 {
        println!("number is non-zero");
    }
}
```
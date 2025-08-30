# If in Let Statement

Can `if` be used in a `let` statement?

---

Yes, but all branches must return the same type.

```rust
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };
    println!("number = {number}");
}
```
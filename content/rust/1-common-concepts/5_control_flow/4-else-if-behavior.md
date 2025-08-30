# Else If Behavior

How does `else if` work in Rust?

---

It checks multiple conditions in sequence, executing only the first true branch.

```rust
fn main() {
    let number = 6;
    if number % 4 == 0 {
        println!("Divisible by 4");
    } else if number % 3 == 0 {
        println!("Divisible by 3");
    } else {
        println!("Other");
    }
}
```
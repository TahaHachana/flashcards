# For Loop Countdown

How can you run a countdown using a `for` loop in Rust?

---

Use a reversed range.

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}
```
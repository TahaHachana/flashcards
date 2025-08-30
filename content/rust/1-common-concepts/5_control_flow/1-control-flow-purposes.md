# Control Flow Purposes

What are the two main purposes of control flow in Rust?

---

To run code conditionally (`if` expressions) and to run code repeatedly (loops).

```rust
fn main() {
    let condition = true;
    if condition {
        println!("Runs conditionally");
    }
    for _ in 0..3 {
        println!("Runs repeatedly");
    }
}
```
# Three Loop Types

What are the three loop types in Rust?

---

`loop`, `while`, and `for`.

```rust
fn main() {
    loop { break; } // infinite unless broken
    while false {}  // runs while condition is true
    for _ in 0..1 {} // iterates over a range
}
```
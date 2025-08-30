# Loop Labels

What are loop labels in Rust used for?

---

To specify which loop `break` or `continue` applies to in nested loops.

```rust
fn main() {
    'outer: loop {
        loop {
            break 'outer;
        }
    }
}
```
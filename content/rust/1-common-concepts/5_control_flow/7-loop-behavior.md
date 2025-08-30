# Loop Behavior

How does `loop` work in Rust?

---

It repeats code indefinitely until explicitly stopped with `break`.

```rust
fn main() {
    loop {
        println!("again!");
        break;
    }
}
```
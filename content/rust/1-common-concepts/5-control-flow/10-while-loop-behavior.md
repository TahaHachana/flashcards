# While Loop Behavior

How does a `while` loop work in Rust?

---

It runs as long as its condition evaluates to `true`.

```rust
fn main() {
    let mut n = 3;
    while n > 0 {
        println!("{n}");
        n -= 1;
    }
}
```
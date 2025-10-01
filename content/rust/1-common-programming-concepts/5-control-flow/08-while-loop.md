## While Loop

How does a `while` loop work in Rust?

---

It runs as long as the condition evaluates to `true`.

```rust
let mut number = 3;
while number != 0 {
    println!("{number}!");
    number -= 1;
}
```


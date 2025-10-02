## While Let Basics

How does `while let` work in Rust?

---

It repeatedly executes a block as long as a value matches a pattern:

```rust
let mut iter = vec![1, 2, 3].into_iter();

while let Some(x) = iter.next() {
    println!("{x}");
}
```


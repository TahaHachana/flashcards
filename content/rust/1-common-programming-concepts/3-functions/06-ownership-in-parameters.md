## Ownership In Parameters

How does ownership apply to function parameters in Rust?

---

Passing parameters follows ownership rules:

* By default, values are moved into the function.
* Use references (`&`) to borrow instead of moving.

```rust
fn print_len(s: &String) {
    println!("{}", s.len());
}
```


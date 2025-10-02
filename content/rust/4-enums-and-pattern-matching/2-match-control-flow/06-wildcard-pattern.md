## Wildcard Pattern

What does the `_` pattern do in `match`?

---

It matches any value without binding. Often used as a fallback arm:

```rust
match n {
    0 => println!("zero"),
    _ => println!("non-zero"),
}
```


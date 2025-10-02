## At Pattern Binding

What does the `@` pattern do in Rust matches?

---

It binds a matched value to a variable while checking a sub-pattern:

```rust
match n {
    val @ 0..=3 => println!("{val} is small"),
    _ => println!("large"),
}
```


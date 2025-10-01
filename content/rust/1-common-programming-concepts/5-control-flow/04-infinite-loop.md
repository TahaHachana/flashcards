## Infinite Loop

How do you write an infinite loop in Rust, and how do you stop it?

---

Use `loop { ... }` for an infinite loop.
Stop it with `break`.

```rust
loop {
    if condition {
        break;
    }
}
```


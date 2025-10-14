## Common Loop Error - Infinite Loop

What's wrong with this code?

```rust
loop {
    println!("Running...");
}
```

---

It runs forever without a break condition, so the program never exits. Add a break condition to exit the loop.


## Question Mark Early Return Behavior

What does it mean that `?` performs an "early return" and why is this important to remember?

---

`?` immediately returns from the function if it encounters an error - any code after the `?` won't execute:

```rust
fn tricky() -> Result<String, String> {
    let result = operation_that_fails()?;
    println!("This never prints if operation fails!");
    Ok(result)
}
```

This is important for:
- Cleanup code (do it before `?`)
- Side effects (they won't happen after a failed `?`)
- Resource management (use RAII patterns or ensure cleanup happens before `?`)


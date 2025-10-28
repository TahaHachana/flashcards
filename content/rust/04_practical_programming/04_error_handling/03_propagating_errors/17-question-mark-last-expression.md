## Question Mark Last Expression

Can you use `?` on the last expression of a function without wrapping in `Ok()`?

---

Yes, if the types align correctly:

```rust
fn get_user_age(id: u32) -> Result<u32, String> {
    // Both return Result, so ? on last expression works
    fetch_user(id)?.age.ok_or("No age specified".into())
}
```

However, you usually need to wrap in `Ok()` when the last operation returns a non-Result value:

```rust
fn calculate() -> Result<i32, String> {
    let a = get_value()?;
    let b = get_value()?;
    Ok(a + b)  // Need Ok() because a + b is just i32
}
```


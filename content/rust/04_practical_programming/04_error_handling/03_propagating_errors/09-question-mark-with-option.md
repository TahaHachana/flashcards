## Question Mark With Option

Can you use `?` with `Option<T>` and what are the rules?

---

Yes! `?` works with `Option` in `Option`-returning functions:

```rust
fn works() -> Option<i32> {
    let opt: Option<i32> = Some(5);
    let value = opt?;  // Returns None if opt is None
    Some(value * 2)
}
```

**Important:** You cannot use `Option`'s `?` in a `Result`-returning function without converting first:

```rust
fn needs_conversion() -> Result<i32, String> {
    let opt: Option<i32> = Some(5);
    let value = opt.ok_or("No value")?;  // Convert first
    Ok(value)
}
```


## Mixing Result And Option

How do you use the `?` operator when you have an `Option` but need to return a `Result`?

---

Convert the `Option` to a `Result` first using `ok_or()` or `ok_or_else()`:

```rust
fn process() -> Result<i32, String> {
    let opt: Option<i32> = Some(5);
    
    // Convert Option to Result
    let value = opt.ok_or("No value found".to_string())?;
    
    Ok(value * 2)
}
```

You cannot directly use `?` on an `Option` in a function returning `Result` without conversion.


## Chaining Operations With Question Mark

How do you chain multiple fallible operations using `?`?

---

Simply use `?` after each operation that can fail:

```rust
fn process_data(path: &str) -> Result<usize, Box<dyn Error>> {
    let contents = std::fs::read_to_string(path)?;
    let trimmed = contents.trim();
    let number: usize = trimmed.parse()?;
    Ok(number * 2)
}
```

If any operation fails, the function immediately returns that error. Only if all succeed does execution reach the final `Ok(...)`.


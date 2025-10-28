## Question Mark Operator Basics

What does the `?` operator do when used with `Result<T, E>`?

---

The `?` operator provides early return on error:

1. If the Result is `Ok(value)`, it unwraps and returns the value
2. If the Result is `Err(e)`, it immediately returns `Err(e)` from the function

```rust
fn read_number() -> Result<i32, Error> {
    let contents = std::fs::read_to_string("file.txt")?;
    let number = contents.trim().parse()?;
    Ok(number)
}
```

The function must return `Result` or `Option` to use `?`.


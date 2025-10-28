## Question Mark Multiple Errors Same Expression

Can you use `?` on both operands in a single expression like `a()? + b()?`?

---

While syntactically valid, it's not recommended and can be confusing:

```rust
// Compiles but unclear evaluation order
fn unclear() -> Result<i32, String> {
    Ok(operation1()? + operation2()?)
}

// Better - explicit and clear
fn clear() -> Result<i32, String> {
    let a = operation1()?;
    let b = operation2()?;
    Ok(a + b)
}
```

The separate version makes it clear that `operation1` is evaluated first, and if it fails, `operation2` never runs.


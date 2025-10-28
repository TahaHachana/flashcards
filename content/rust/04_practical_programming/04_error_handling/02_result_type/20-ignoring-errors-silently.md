## Ignoring Errors Silently

What's wrong with ignoring errors using `let _ = ...` and what should you do instead?

---

**Bad - silently ignores:**
```rust
fn process() {
    let _ = some_operation();  // Error thrown away!
}
```

**Better options:**

Propagate it:
```rust
fn process() -> Result<(), Error> {
    some_operation()?;
    Ok(())
}
```

Or explicitly handle/log:
```rust
if let Err(e) = some_operation() {
    eprintln!("Warning: {}", e);
}
```

Ignoring errors hides bugs and makes debugging difficult.


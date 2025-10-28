## Result Ownership In Errors

How does ownership affect values used in both success and error paths?

---

Be careful not to move values when constructing errors if you need them later:

**Problem:**
```rust
fn process(data: String) -> Result<String, String> {
    if data.is_empty() {
        return Err(format!("Empty: {}", data));  // data moved!
    }
    Ok(data.to_uppercase())  // Can't use data here
}
```

**Solution:**
```rust
fn process(data: String) -> Result<String, String> {
    if data.is_empty() {
        return Err("Data is empty".into());  // Don't move data
    }
    Ok(data.to_uppercase())  // data still available
}
```


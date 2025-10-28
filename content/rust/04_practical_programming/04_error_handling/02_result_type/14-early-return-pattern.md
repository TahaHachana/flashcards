## Early Return Pattern

How do you use early returns for validation in Rust functions?

---

Return `Err` immediately when validation fails:

```rust
fn validate_age(age: i32) -> Result<i32, String> {
    if age < 0 {
        return Err("Age cannot be negative".into());
    }
    if age > 150 {
        return Err("Age unrealistic".into());
    }
    Ok(age)
}

fn process(age: i32) -> Result<(), String> {
    let valid_age = validate_age(age)?;  // Propagates error
    println!("Valid age: {}", valid_age);
    Ok(())
}
```


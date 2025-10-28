## Cascading Unwraps Problem

What's wrong with chaining multiple `unwrap()` calls and how do you fix it?

---

**Bad - unclear which operation failed:**
```rust
let value = config.get("key").unwrap()
    .parse::<i32>().unwrap();
```

**Good - clear error messages:**
```rust
let key = config.get("key")
    .expect("Config must contain 'key'");
let value = key.parse::<i32>()
    .expect("Key value must be a valid integer");
```

**Better - proper error handling:**
```rust
let key = config.get("key")
    .ok_or("Missing key")?;
let value = key.parse::<i32>()
    .map_err(|e| format!("Invalid integer: {}", e))?;
```

Cascading unwraps hide which operation failed. Use separate statements with `expect()` or proper error handling.


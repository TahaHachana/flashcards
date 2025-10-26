## Option<T> Enum

What is Option<T>, why does it exist in Rust, and what are three ways to extract its value safely?

---

**Definition**:
```rust
enum Option<T> {
    None,
    Some(T),
}
```

**Why it exists**: Rust has no null. `Option` represents "might not have a value."

**Three safe extraction methods**:

1. **Pattern matching**:
```rust
match maybe_value {
    Some(v) => println!("Got: {}", v),
    None => println!("Nothing"),
}
```

2. **unwrap_or** (provide default):
```rust
let value = maybe_value.unwrap_or(0);
```

3. **if let**:
```rust
if let Some(v) = maybe_value {
    println!("Got: {}", v);
}
```

Avoid `unwrap()` and `expect()` in production - they panic on None.


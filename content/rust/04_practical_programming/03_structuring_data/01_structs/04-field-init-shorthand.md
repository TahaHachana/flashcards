## Field Init Shorthand

What is the field init shorthand in Rust and when can you use it?

---

When variable names match field names, you can omit the field name:

```rust
fn create_user(username: String, email: String) -> User {
    User {
        username,  // Instead of username: username
        email,     // Instead of email: email
        age: 0,
        active: true,
    }
}
```

This only works when the variable name **exactly matches** the field name.


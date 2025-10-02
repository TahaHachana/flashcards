## Field Init Shorthand

What is field init shorthand in Rust structs?

---

When parameter names match field names, you can omit repetition:

```rust
fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username, // shorthand
        email,
        sign_in_count: 1,
    }
}
```


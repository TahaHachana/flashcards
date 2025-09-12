# Field Init Shorthand

What is the field init shorthand when constructing a struct?

---

If variable (or parameter) names match field names, you can omit `field: field` and just write the identifier once. Rust automatically assigns the variable with the same name to that field.

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,      // same as: username: username
        email,         // same as: email: email
        sign_in_count: 1,
    }
}

let user = build_user(String::from("a@example.com"), String::from("alice"));
```

Benefits:
- Reduces repetition and visual noise.
- Encourages field names that align with conceptual parameter names.
- Works only when the variable is in scope and has the exact same identifier as the field.
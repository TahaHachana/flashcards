## Classic Struct Syntax

How do you define and instantiate a classic struct with named fields in Rust?

---

Define with named fields and types:
```rust
struct User {
    username: String,
    email: String,
    age: u32,
    active: bool,
}
```

Instantiate by providing values for all fields:
```rust
let user = User {
    username: String::from("alice"),
    email: String::from("alice@example.com"),
    age: 30,
    active: true,
};
```

Access fields using dot notation: `user.username`


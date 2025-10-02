## Creating Instances

How do you create an instance of a struct in Rust?

---

Use `key: value` pairs, in any order:

```rust
let user1 = User {
    active: true,
    username: String::from("name"),
    email: String::from("email@example.com"),
    sign_in_count: 1,
};
```


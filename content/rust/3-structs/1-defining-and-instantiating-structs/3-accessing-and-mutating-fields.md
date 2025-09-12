# Accessing and Mutating Fields

How do you read and change struct fields?

---

Use dot notation. To change fields, the entire instance must be declared `mut`.

```rust
let mut user1 = User {
    active: true,
    username: String::from("name"),
    email: String::from("old@example.com"),
    sign_in_count: 1,
};

user1.email = String::from("new@example.com");
println!("{}", user1.email);
```

Note: Individual fields can’t be marked `mut`; mutability is attached to the binding (`let mut user1`).
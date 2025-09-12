# Instantiating a Struct

How do you create an instance of a struct, and does field order matter?

---

Provide `field: value` pairs inside braces after the struct name. Field order does not matter; Rust matches by field names, not position.

```rust
let user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
};
```

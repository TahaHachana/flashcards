# Defining a Struct

How do you define a struct in Rust?

---

Use the `struct` keyword, name the struct, and list its fields and types inside braces.

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

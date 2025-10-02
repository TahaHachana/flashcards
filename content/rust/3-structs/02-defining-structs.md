## Defining Structs

How do you define a struct with named fields in Rust?

---

Use the `struct` keyword followed by field definitions:

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```


# Struct Update Syntax

How do you create a new struct instance using fields from an existing one?

---

Use `..existing_instance` to fill in the remaining fields from another instance. This performs a field-by-field move (or copy for `Copy` types). Non-`Copy` fields (e.g. `String`) are moved, so you can no longer use them through the original instance afterward.

```rust
#[derive(Debug)]
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

let user1 = User {
    active: true,
    username: String::from("alice"),
    email: String::from("alice@example.com"),
    sign_in_count: 1,
};

let user2 = User {
    email: String::from("new@example.com"),
    ..user1
};

// user1.username and user1.email were moved; user1 cannot be fully reused.
// println!("{}", user1.username); // <-- would be a compile error
println!("{:?}", user2);
```

Key points:
- You must specify at least one field before `..user1` (cannot be the only part).
- Order: explicitly set fields first, then `..source`.
- If all remaining fields are `Copy`, the original instance stays usable.
## Struct Update Syntax

How does the struct update syntax work in Rust, and what ownership consideration must you be aware of?

---

Use `..other_struct` to copy remaining fields from another instance:

```rust
let user2 = User {
    username: String::from("bob"),
    email: String::from("bob@example.com"),
    ..user1  // Copy age and active from user1
};
```

**Critical ownership consideration**: Non-Copy types are **moved**. After this code, `user1.username` and `user1.email` are no longer valid (moved), but `user1.age` and `user1.active` are still usable (they're Copy types).


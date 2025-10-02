## Struct Update Syntax

How do you reuse fields from another struct instance?

---

Use struct update syntax with `..`:

```rust
let user2 = User {
    email: String::from("new@example.com"),
    ..user1
};
```

Fields not listed are moved from `user1` unless they implement `Copy`.


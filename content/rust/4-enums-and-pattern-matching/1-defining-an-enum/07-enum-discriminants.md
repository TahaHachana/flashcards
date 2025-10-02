## Enum Discriminants

What are discriminants in enums and how do you set them?

---

Discriminants are explicit integer values for C-like enums:

```rust
enum Status {
    Ok = 0,
    NotFound = 1,
    Forbidden = 2,
}
```

They can be accessed with casts, e.g., `Status::Ok as i32`.


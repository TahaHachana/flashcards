## Struct Ownership and Drop

How does ownership work with structs, and what happens when a struct goes out of scope?

---

Structs **own their data**. When a struct goes out of scope:
1. The struct's `Drop` implementation runs (if any)
2. All fields are dropped in declaration order
3. Non-Copy types in the struct are moved when the struct is moved

```rust
struct User {
    username: String,  // Owned data
    age: u32,
}

{
    let user = User { /* ... */ };
    // user owns its String
} // user goes out of scope, String is dropped
```

If the struct contains non-Copy types, moving the struct moves those fields, making the original invalid.


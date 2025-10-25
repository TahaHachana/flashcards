## Common Mistake - Forgetting Conversion

Why does this code fail and how do you fix it?
```rust
struct User {
    name: String,
}

let u = User {
    name: "Alice",
};
```

---

"Alice" is a &str literal, but the struct expects String. Fix by converting:
```rust
let u = User {
    name: "Alice".to_string(),  // Convert &str to String
};
```
Or use String::from("Alice"). The struct owns the data, so it needs String, not a reference.


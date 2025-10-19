## Custom Struct Copy Rule

When can a custom struct be Copy?

---

Only if all fields are Copy. If any field uses move semantics, the entire struct must use move semantics.

```rust
struct Point { x: i32, y: i32 }  // Can be Copy
struct User { name: String }      // Cannot be Copy
```


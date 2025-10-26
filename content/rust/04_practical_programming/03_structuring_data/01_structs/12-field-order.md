## Struct Field Order in Initialization

Does the order of fields matter when instantiating a struct in Rust?

---

**No**, field order doesn't matter during instantiation:

```rust
struct User {
    username: String,
    age: u32,
    active: bool,
}

// All valid - any order works
let user = User {
    age: 30,
    username: String::from("alice"),
    active: true,
};
```

However, it's **conventional** to match the order in the struct definition for readability. The compiler only requires that all fields are initialized exactly once.


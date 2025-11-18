## Why Trait Objects Exist

What problem do trait objects solve?

---

Trait objects solve the **heterogeneous collections** problem - storing values of different types together when they share common behavior.

```rust
// ❌ Without trait objects - can't mix types
let items = vec![String::from("hello"), 42];  // Error!

// ✅ With trait objects - can mix types
let items: Vec<Box<dyn Display>> = vec![
    Box::new(String::from("hello")),
    Box::new(42),
    Box::new("world"),
];
```

Different types, same interface.


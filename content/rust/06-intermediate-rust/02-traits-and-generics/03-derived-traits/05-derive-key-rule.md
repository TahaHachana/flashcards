## The Key Rule for Deriving

What is the key rule for deriving a trait on a type?

---

**You can only derive a trait if ALL fields of your type implement that trait.**

Example:
```rust
#[derive(Clone)]
struct Works {
    field1: i32,     // ✅ i32 implements Clone
    field2: String,  // ✅ String implements Clone
}

#[derive(Copy)]
struct Fails {
    field: String,   // ❌ String does NOT implement Copy
}
// Error: cannot derive Copy
```


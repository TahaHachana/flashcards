## Creating Immutable References

How do you create an immutable reference?

---

Use & before the value.

```rust
let s = String::from("hello");
let r = &s;  // r is &String
```


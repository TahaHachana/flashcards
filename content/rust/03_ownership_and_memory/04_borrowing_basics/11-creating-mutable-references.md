## Creating Mutable References

How do you create a mutable reference?

---

The original variable must be mut, then use &mut.

```rust
let mut s = String::from("hello");
let r = &mut s;  // Mutable reference
```


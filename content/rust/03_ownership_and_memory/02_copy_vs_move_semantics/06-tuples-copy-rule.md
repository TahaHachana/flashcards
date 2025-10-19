## Tuples Copy Rule

When is a tuple Copy?

---

Only if all its elements are Copy. If any element uses move semantics, the entire tuple does too.

```rust
let a: (i32, i32) = (1, 2);        // Copy
let b: (i32, String) = (1, s);     // NOT Copy
```


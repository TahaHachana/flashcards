## String vs &str

What's the difference between String and &str?

---

String: owned, heap-allocated, growable, can be modified. &str: borrowed reference, immutable, points to existing string data.

```rust
let owned = String::from("hello");
let borrowed: &str = &owned;
```


## Option Ownership

What happens to ownership when you move an `Option<T>`?

---

`Option<T>` owns its inner value `T`. When you move the `Option`, you move the inner value:

```rust
let opt = Some(String::from("hello"));
let moved = opt;  // opt is moved, can't use it anymore

// opt is no longer valid here
```

To keep the original, use:
- `as_ref()` to work with references
- `.clone()` if `T` implements `Clone`
- `.copied()` if `T` implements `Copy`


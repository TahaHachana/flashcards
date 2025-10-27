## Flatten Method

What does the `flatten()` method do on nested Options?

---

`flatten()` collapses `Option<Option<T>>` into `Option<T>`:

```rust
let nested = Some(Some(5));
let flat = nested.flatten();  // Some(5)

let none_inner = Some(None);
let flat = none_inner.flatten();  // None

let none_outer: Option<Option<i32>> = None;
let flat = none_outer.flatten();  // None
```

Any `None` at either level results in `None`.


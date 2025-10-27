## Unwrap Or Method

What does the `unwrap_or()` method do on an `Option<T>`?

---

`unwrap_or(default)` returns the value inside `Some` if it exists, otherwise returns the provided default value:

```rust
let value = Some(10).unwrap_or(0);    // 10
let value = None.unwrap_or(0);        // 0
```

It's a safe alternative to `unwrap()` because it never panics.


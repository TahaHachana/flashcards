## Unwrap Danger

Why should you avoid using `unwrap()` on `Option<T>` in production code?

---

`unwrap()` panics (crashes the program) if called on `None`:

```rust
let value: Option<i32> = None;
let x = value.unwrap(); // PANIC!
```

Better alternatives:
- `unwrap_or(default)` - provide a default
- `match` or `if let` - handle both cases
- `?` operator - propagate the None
- `expect("message")` - only for debugging with a better error message

Only use `unwrap()` in tests or when you're absolutely certain the value exists.


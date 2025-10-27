## Unwrap Or Else Method

When should you use `unwrap_or_else()` instead of `unwrap_or()`?

---

Use `unwrap_or_else()` when computing the default value is expensive or has side effects:

```rust
// unwrap_or evaluates the default immediately (eager)
value.unwrap_or(expensive_computation())  // Always computed

// unwrap_or_else only computes if needed (lazy)
value.unwrap_or_else(|| expensive_computation())  // Only if None
```

The closure passed to `unwrap_or_else()` is only called when the `Option` is `None`.


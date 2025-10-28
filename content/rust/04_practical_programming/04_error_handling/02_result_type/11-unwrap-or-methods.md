## Unwrap Or Methods

What's the difference between `unwrap_or()` and `unwrap_or_else()` on Results?

---

`unwrap_or(default)`: Returns the value or a provided default (eager evaluation)
```rust
let value = result.unwrap_or(0);  // Always evaluates 0
```

`unwrap_or_else(closure)`: Computes default only if needed (lazy evaluation)
```rust
let value = result.unwrap_or_else(|err| {
    eprintln!("Error: {}", err);  // Only runs on Err
    0
});
```

Use `unwrap_or_else()` when computing the default is expensive or has side effects.


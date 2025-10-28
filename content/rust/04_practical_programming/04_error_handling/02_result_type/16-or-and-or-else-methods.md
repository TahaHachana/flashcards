## Or And Or Else Methods

What do `or()` and `or_else()` do with Results?

---

They provide fallback Results if the original is an error:

`or()`: Returns the original if `Ok`, otherwise returns the provided alternative
```rust
let primary: Result<i32, &str> = Err("failed");
let backup: Result<i32, &str> = Ok(42);
let result = primary.or(backup);  // Ok(42)
```

`or_else()`: Like `or()` but computes the alternative lazily
```rust
let result = primary.or_else(|_| Ok(0));  // Ok(0)
```

Useful for fallback strategies or retry logic.


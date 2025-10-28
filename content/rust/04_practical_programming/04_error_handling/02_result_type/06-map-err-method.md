## Map Err Method

What does the `map_err()` method do on a `Result<T, E>`?

---

`map_err()` transforms the error value if the Result is `Err`, leaving `Ok` unchanged:

```rust
let result: Result<i32, &str> = Err("file not found");

let mapped = result.map_err(|e| format!("Error: {}", e));
// Err("Error: file not found")
```

Useful for adding context to errors or converting between error types.


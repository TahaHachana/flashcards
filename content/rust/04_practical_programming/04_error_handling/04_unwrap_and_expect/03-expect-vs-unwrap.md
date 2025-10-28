## Expect Vs Unwrap

What's the difference between `unwrap()` and `expect()`, and when should you prefer one over the other?

---

`expect()` is like `unwrap()` but lets you provide a custom panic message:

```rust
let result: Result<i32, &str> = Err("file not found");

result.unwrap();  
// PANIC: called `Result::unwrap()` on an `Err` value: "file not found"

result.expect("Configuration file must exist");
// PANIC: Configuration file must exist: "file not found"
```

**Prefer `expect()` over `unwrap()`** because:
- It makes debugging easier with context
- It documents why you believe it's safe
- It explains the invariant being assumed

Always use `expect()` with a meaningful message in production code.


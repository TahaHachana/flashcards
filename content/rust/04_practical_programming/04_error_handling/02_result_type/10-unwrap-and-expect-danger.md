## Unwrap And Expect Danger

Why should you avoid `unwrap()` and when is `expect()` appropriate?

---

`unwrap()` panics (crashes) if the Result is `Err`, making it dangerous in production:

```rust
let result: Result<i32, &str> = Err("failed");
// let x = result.unwrap(); // PANIC!
```

**When to use:**
- In tests
- In examples/prototypes
- When you've proven the error is impossible (document why!)

**Better alternatives:**
- `expect("context message")` for debugging (includes your message)
- Pattern matching or `?` for production
- `unwrap_or()` or `unwrap_or_else()` to provide defaults


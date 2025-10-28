## And Then Method On Result

What is `and_then()` used for with `Result<T, E>` and why is it needed?

---

`and_then()` chains operations that themselves return `Result`. It's used when your transformation function returns a `Result`:

```rust
fn parse(s: &str) -> Result<i32, String> { ... }
fn validate(n: i32) -> Result<i32, String> { ... }

let result = parse("42")
    .and_then(|n| validate(n));  // Chain results
```

Unlike `map()`, it prevents nested `Result<Result<T, E>, E>` by flattening the result.


## Matches Macro

What does the `matches!` macro return and when is it useful?

---

It returns a boolean indicating if a value matches a pattern:

```rust
let token = Some(42);

if matches!(token, Some(_)) {
    println!("Token is present");
}
```

Useful for simple condition checks without binding values.


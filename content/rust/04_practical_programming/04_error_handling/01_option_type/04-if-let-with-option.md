## If Let With Option

When should you use `if let` with `Option<T>` instead of `match`?

---

Use `if let` when you only care about one case (usually the `Some` case):

```rust
if let Some(value) = maybe_value {
    // Only handle Some case
    println!("{}", value);
}
// No else needed if you don't care about None
```

It's more concise than `match` when you don't need to handle both variants.


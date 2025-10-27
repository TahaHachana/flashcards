## Pattern Matching With Option

How do you safely extract a value from an `Option<T>` using pattern matching?

---

Use a `match` expression to handle both cases:

```rust
match some_option {
    Some(value) => {
        // Use value here
    }
    None => {
        // Handle the absence case
    }
}
```

The compiler enforces that you handle both `Some` and `None` cases (exhaustive matching).


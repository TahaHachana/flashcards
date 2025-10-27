## Question Mark Operator With Option

How does the `?` operator work with `Option<T>`?

---

The `?` operator provides early return: if the `Option` is `None`, it immediately returns `None` from the function. If it's `Some`, it unwraps the value:

```rust
fn get_first_word(text: Option<&str>) -> Option<&str> {
    let text = text?;  // Returns None if text is None
    text.split_whitespace().next()
}
```

The function must return `Option<T>` to use `?`.


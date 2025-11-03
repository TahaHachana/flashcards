## Owned vs Borrowed Fields

Which fields in this struct require lifetime parameters, and why?
```rust
struct Document<'a> {
    title: String,
    author: &'a str,
    content: Vec<String>,
}
```

---

Only `author` requires a lifetime parameter because it's a borrowed reference. The `title` and `content` fields are owned data (String, Vec) and don't constrain the struct's lifetime. Only borrowed fields require lifetime parameters—owned data doesn't affect when the struct can exist.


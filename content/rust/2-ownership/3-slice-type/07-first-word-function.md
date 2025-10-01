## First Word Function

Why is returning a slice safer than returning an index for the first word in a string?

---

Slices are tied to the original data’s lifetime, so they stay valid only while the data is valid.
Returning an index can become invalid if the string changes.

```rust
fn first_word(s: &String) -> &str { /* ... */ }
```


## Gotcha Missing Iterator Lifetime Bound

What's missing from this signature, and why is it needed?

```rust
fn get_words<'a>(text: &'a str) -> impl Iterator<Item = &'a str> {
    text.split_whitespace()
}
```

---

Missing the `+ 'a` bound on the return type. Should be:
```rust
impl Iterator<Item = &'a str> + 'a
```
The `+ 'a` ensures the iterator type itself doesn't outlive the borrowed data. Without it, the iterator could theoretically live longer than the data it borrows from, which would be unsafe.


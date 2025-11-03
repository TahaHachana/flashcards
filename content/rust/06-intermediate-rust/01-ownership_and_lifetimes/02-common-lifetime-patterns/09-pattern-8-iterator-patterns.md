## Pattern 8 Iterator Patterns

What is the correct signature for a function returning an iterator over borrowed data, and why is the `+ 'a` bound necessary?

```rust
fn get_words<'a>(text: &'a str) -> impl Iterator<Item = &'a str> + 'a {
    text.split_whitespace()
}
```

---

Return type is `impl Iterator<Item = &'a T> + 'a`. The `+ 'a` bound means the iterator itself can't outlive the data it borrows from. Items yielded have lifetime tied to input. Without the `+ 'a`, the iterator type could theoretically live longer than the borrowed data. Mental shortcut: "Iterator yields borrowed slices" → lifetime propagates.


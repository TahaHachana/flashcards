## Gotcha Iterator Return Types

What's missing from this iterator function signature, and why is it required?

```rust
fn get_words(text: &str) -> impl Iterator<Item = &str> {
    text.split_whitespace()
}
```

---

Missing the lifetime bound `+ 'a`. The correct signature is:
```rust
fn get_words<'a>(text: &'a str) -> impl Iterator<Item = &'a str> + 'a {
    text.split_whitespace()
}
```
The `+ 'a` bound can't be elided—it must be explicit to ensure the iterator type itself doesn't outlive the borrowed data it yields from.


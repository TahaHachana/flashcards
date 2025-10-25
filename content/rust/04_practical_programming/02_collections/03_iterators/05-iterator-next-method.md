## Iterator Next Method

What does `.next()` return and how does it work?

---

Returns `Option<T>`:
- `Some(value)` if items remain
- `None` when iterator is exhausted

```rust
let mut iter = vec![1, 2].iter();
assert_eq!(iter.next(), Some(&1));
assert_eq!(iter.next(), Some(&2));
assert_eq!(iter.next(), None);  // Stays None forever
```


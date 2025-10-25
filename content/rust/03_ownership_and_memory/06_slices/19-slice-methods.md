## Slice Methods

What are some useful slice methods?

---

len(), is_empty(), first(), last(), get() (safe access), split_at() (split into two), chunks() (iterate in chunks).

```rust
slice.len();       // Length
slice.get(2);      // Some(&value) or None
slice.split_at(2); // (left, right)
```


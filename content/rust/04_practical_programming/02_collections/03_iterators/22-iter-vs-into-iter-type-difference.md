## Iter vs Into Iter Type Difference

What's the difference in closure parameter types between `.iter()` and `.into_iter()`?

---

```rust
// .iter() - parameter is &T
vec.iter().for_each(|x| {
    // x is &i32
});

// .into_iter() - parameter is T
vec.into_iter().for_each(|x| {
    // x is i32 (owned)
});
```


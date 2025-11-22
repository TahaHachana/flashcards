## Adaptor Pattern Internal Structure

How do iterator adaptors work internally? Show the pattern with a Map adaptor example.

---

Every adaptor follows the decorator pattern - wrapping an iterator in a struct that implements Iterator:

```rust
struct Map<I, F> {
    iter: I,     // Wrapped iterator
    func: F,     // Transformation function
}

impl<I, F, B> Iterator for Map<I, F>
where
    I: Iterator,
    F: FnMut(I::Item) -> B,
{
    type Item = B;
    
    fn next(&mut self) -> Option<B> {
        self.iter.next().map(|x| (self.func)(x))
    }
}
```

**Key mechanisms:**

1. **Wrapping**: Each adaptor contains the previous iterator
2. **Delegation**: `next()` calls `next()` on wrapped iterator
3. **Transformation**: Applies its operation to each element
4. **Nested types**: Creates type like `Filter<Map<Iter<i32>>>`

When you call `.next()` on the outermost adaptor, it cascades through all wrapped iterators, applying each transformation in sequence.

This is why multiple operations fuse into a single pass through the data.


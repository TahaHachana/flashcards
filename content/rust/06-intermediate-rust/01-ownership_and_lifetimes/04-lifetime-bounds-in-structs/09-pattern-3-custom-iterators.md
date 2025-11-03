## Pattern 3 Custom Iterators

How do custom iterators use struct lifetime parameters?

---

Custom iterators hold a reference to data with lifetime `'a`, maintain position/state, implement the `Iterator` trait, and yield items with lifetime `'a`. Example:
```rust
struct Chunks<'a> {
    data: &'a [u8],
    chunk_size: usize,
}

impl<'a> Iterator for Chunks<'a> {
    type Item = &'a [u8];
    fn next(&mut self) -> Option<Self::Item>
}
```
This enables lazy iteration over borrowed data.


## Slices for Subranges

How do you pass part of a collection to a function?

---

Use slices with range syntax.

```rust
fn process_half(data: &[i32]) { }
let vec = vec![1, 2, 3, 4, 5, 6];
process_half(&vec[..3]);  // First half
```


## Finding Boundaries with char_indices

What does char_indices() return and how does it help find valid boundaries?

---

```rust
let s = String::from("café");
let indices: Vec<usize> = s.char_indices()
    .map(|(i, _)| i)
    .collect();
println!("{:?}", indices);  // [0, 1, 2, 3, 5]
```
char_indices() returns (byte_index, char) tuples. Notice no index 4 - it would be in the middle of 'é'. These indices are all valid slice boundaries.


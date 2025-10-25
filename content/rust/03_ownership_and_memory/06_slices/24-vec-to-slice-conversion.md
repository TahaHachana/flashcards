## Vec to Slice Conversion

How do you get a slice from a Vec?

---

Multiple ways: &vec, &vec[..], or vec.as_slice().

```rust
let vec = vec![1, 2, 3];
let slice: &[i32] = &vec;
let slice = &vec[..];
let slice = vec.as_slice();
```


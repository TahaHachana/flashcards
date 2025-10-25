## Slices Cannot Outlive Data

Can slices outlive the data they reference?

---

No. Same lifetime rules as references - slices can't outlive their data.

```rust
let slice;
{
    let vec = vec![1, 2, 3];
    slice = &vec[..];  // ❌ Error: vec doesn't live long enough
}
```


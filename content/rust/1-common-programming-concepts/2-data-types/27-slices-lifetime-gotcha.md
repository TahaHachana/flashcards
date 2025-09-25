## Slices Lifetime Gotcha

Why must you be careful with slices and lifetimes?

---

Slices borrow the original data but don’t own it.
If the owner goes out of scope, the slice becomes invalid.

Example:

```rust
let slice: &[i32];
{
    let arr = [1, 2, 3];
    slice = &arr[0..2]; // borrows arr
}
// println!("{:?}", slice); // error: arr dropped
```


## One Function Multiple Types

Why can one function with &[T] parameter work with both arrays and vectors?

---

&[T] is a general slice type that works with any contiguous sequence. Arrays and vectors can both be sliced into &[T].

```rust
fn sum(s: &[i32]) -> i32 { }
sum(&arr[..]);  // Works with arrays
sum(&vec[..]);  // Works with vectors
```


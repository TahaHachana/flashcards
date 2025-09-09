# Array Slices

How do you slice a Rust array, and what is the slice type?

---

Use `[start..end]` syntax on an array reference. The slice type is `&[T]`, storing a pointer and length:

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let slice: &[i32] = &a[2..5];
    assert_eq!(slice, &[30, 40, 50]);
    println!("Slice of array: {:?}", slice);
}
```
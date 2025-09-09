# Slice Basics

What is a slice in Rust?

---

A slice is a reference to a contiguous sequence of elements in a collection, composed of a pointer to the first element and a length. It does not own its data and has its lifetime tied to the underlying collection.

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
    let slice = &a[1..4];
    assert_eq!(slice, &[2, 3, 4]);
    println!("Array slice: {:?}", slice);
}
```
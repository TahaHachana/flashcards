## Array Slice Type

What is the type of an array or Vec slice?

---

&[T] where T is the element type.

```rust
let arr = [1, 2, 3, 4, 5];
let slice: &[i32] = &arr[1..3];  // [2, 3]
```


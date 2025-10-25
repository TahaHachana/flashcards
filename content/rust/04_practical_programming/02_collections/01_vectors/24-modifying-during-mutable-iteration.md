## Modifying During Mutable Iteration

How do you double every element in a `Vec<i32>` in place?

---

```rust
let mut vec = vec![1, 2, 3, 4];
for num in vec.iter_mut() {
    *num *= 2;  // Dereference to modify
}
// vec is now [2, 4, 6, 8]
```
Use `.iter_mut()` and dereference with `*` to modify.


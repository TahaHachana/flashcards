## Iter Mut Dereferencing

Why do you need `*` when modifying values with `.iter_mut()`?

---

`.iter_mut()` returns `&mut T` (mutable references), not values. To modify the actual value, you must dereference:
```rust
for num in vec.iter_mut() {
    *num += 1;  // Dereference to modify
}
```
Without `*`, you'd try to operate on a reference, which won't work.


## Iter Mut Modify Pattern

Show how to double all values in a vector in place using iterators.

---

```rust
let mut vec = vec![1, 2, 3, 4, 5];

vec.iter_mut().for_each(|x| *x *= 2);
// vec is now [2, 4, 6, 8, 10]

// Or with for loop:
for x in vec.iter_mut() {
    *x *= 2;
}
```
Must use `.iter_mut()` and dereference with `*`.


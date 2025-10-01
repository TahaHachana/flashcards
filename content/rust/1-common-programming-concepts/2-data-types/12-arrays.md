## Arrays

What are arrays in Rust and how do they behave?

---

* Fixed size, all elements same type.
* Accessed by index.
* Out-of-bounds indexing causes a runtime panic.
* Arrays are distinct from vectors (`Vec<T>`), which are growable.

```rust
let a = [1, 2, 3, 4, 5];
let first = a[0];
```


## Double Reference in Filter

Why do you often need `|&&x|` in `.filter()` when using `.iter()`?

---

`.iter()` gives `&T`, so the closure parameter is `&&T`:
```rust
vec.iter()
    .filter(|&&x| x > 5)  // x is &&i32
```
First `&` is from closure parameter, second `&` is from `.iter()`.

Alternative: `|x| **x > 5` (double dereference)


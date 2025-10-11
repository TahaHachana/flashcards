## Scalar Types Are Copy

What happens when you assign or pass a scalar type to a function?

---

Scalar types implement Copy, so they're copied rather than moved. The original remains valid.

```rust
let x = 5;
let y = x;  // x is copied, both x and y are valid
```


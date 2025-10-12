## Nested Tuples

Can tuples contain other tuples?

---

Yes. Tuples can be nested. Access using chained dot notation.

```rust
let nested = ((1, 2), (3, 4));
let first_pair = nested.0;  // (1, 2)
let first_element = nested.0.0;  // 1
```


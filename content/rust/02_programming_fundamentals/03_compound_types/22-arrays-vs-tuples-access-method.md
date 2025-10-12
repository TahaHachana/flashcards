## Arrays vs Tuples Access Method

How do access methods differ between arrays and tuples?

---

Arrays use bracket notation (arr[0]), tuples use dot notation (tup.0).

```rust
let arr = [1, 2, 3];
let first_arr = arr[0];

let tup = (1, 2, 3);
let first_tup = tup.0;
```


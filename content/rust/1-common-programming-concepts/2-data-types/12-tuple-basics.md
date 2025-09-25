## Tuple Basics

How do you declare and destructure a tuple in Rust?

---

Declare:

```rust
let tup: (i32, f64, u8) = (500, 6.4, 1);
```

Destructure:

```rust
let (x, y, z) = tup;
```

Access by index: `tup.0`, `tup.1`, `tup.2`


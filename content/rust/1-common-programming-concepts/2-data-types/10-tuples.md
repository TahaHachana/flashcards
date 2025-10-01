## Tuples

What are tuples in Rust and how are they used?

---

* Fixed length, can contain mixed types.
* Values can be accessed via destructuring or by index.

```rust
let tup: (i32, f64, u8) = (500, 6.4, 1);
let (x, y, z) = tup;
println!("y = {y}");
```


## Destructuring Tuples

How do you destructure a tuple into separate variables?

---

Use pattern matching with let binding.

```rust
let tup = (500, 6.4, 1);
let (x, y, z) = tup;
println!("{}, {}, {}", x, y, z);  // 500, 6.4, 1
```


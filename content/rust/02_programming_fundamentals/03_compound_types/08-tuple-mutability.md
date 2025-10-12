## Tuple Mutability

How do you modify tuple elements?

---

Make the tuple mutable, then assign to specific elements. Size and types cannot change.

```rust
let mut tup = (1, 2, 3);
tup.0 = 10;
println!("{:?}", tup);  // (10, 2, 3)
```


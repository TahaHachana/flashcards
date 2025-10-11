## Floating-Point Precision Issues

Why should you never compare floating-point numbers for exact equality?

---

Floating-point arithmetic has inherent precision limitations. Compare if values are close enough instead.

```rust
let x = 0.1 + 0.2;  // 0.30000000000000004
let y = 0.3;
println!("{}", x == y);  // false!
println!("{}", (x - y).abs() < 0.00001);  // true
```


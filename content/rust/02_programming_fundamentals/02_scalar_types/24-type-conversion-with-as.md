## Type Conversion with as

How do you convert between numeric types?

---

Use the as keyword for explicit conversion. Be careful with narrowing conversions.

```rust
let integer: i32 = 10;
let float = integer as f64;
let large: i32 = 300;
let small = large as i8;  // Truncates to 44
```


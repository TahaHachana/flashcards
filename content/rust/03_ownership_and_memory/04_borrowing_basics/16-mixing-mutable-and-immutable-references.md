## Mixing Mutable and Immutable References

Can you have mutable and immutable references active at the same time?

---

No. Immutable references expect data won't change, but mutable references can change it, violating expectations.

```rust
let r1 = &s;      // Immutable
let r2 = &mut s;  // ❌ Error
println!("{}", r1);
```


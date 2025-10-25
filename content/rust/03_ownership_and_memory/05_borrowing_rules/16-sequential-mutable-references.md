## Sequential Mutable References

Can you have multiple mutable references if they don't overlap in time?

---

Yes. As long as they're not active simultaneously.

```rust
let r1 = &mut s;
println!("{}", r1);  // Last use
let r2 = &mut s;  // ✅ OK: r1 no longer active
```


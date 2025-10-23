## Reference Scope Until Last Use

How long are references valid?

---

From where they're created until their last use, not necessarily the end of scope. The compiler tracks when references are actually used.

```rust
let r1 = &s;
println!("{}", r1);  // Last use
let r2 = &mut s;  // ✅ OK: r1 no longer active
```


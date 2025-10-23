## Non-Overlapping Mutable Borrows

When can you create a second mutable reference?

---

After the first mutable reference's last use, not necessarily after its scope ends.

```rust
let r1 = &mut s;
println!("{}", r1);  // Last use of r1
let r2 = &mut s;  // ✅ OK: r1 no longer used
```


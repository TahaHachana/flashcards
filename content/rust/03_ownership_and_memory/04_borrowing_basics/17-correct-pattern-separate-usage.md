## Correct Pattern Separate Usage

How do you use both immutable and mutable references correctly?

---

Use immutable references first, then after their last use, create mutable reference.

```rust
let r1 = &s;
println!("{}", r1);  // Last use of r1
let r2 = &mut s;  // ✅ OK: r1 done
```


## Borrowing Prevents Moving

Can you move a value while it's borrowed?

---

No. If move were allowed, references would become dangling.

```rust
let r = &s;
let s2 = s;  // ❌ Error: can't move while borrowed
println!("{}", r);
```


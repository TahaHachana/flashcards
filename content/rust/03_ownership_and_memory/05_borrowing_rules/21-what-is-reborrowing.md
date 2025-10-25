## What is Reborrowing

What is reborrowing?

---

Creating a new reference from an existing mutable reference. Allows temporary sharing while maintaining the original reference.

```rust
let r1 = &mut x;
let r2 = &mut *r1;  // Reborrow
*r2 = 10;
*r1 = 20;  // r1 still valid
```


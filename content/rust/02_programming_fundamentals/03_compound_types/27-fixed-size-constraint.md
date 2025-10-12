## Fixed Size Constraint

Can you change the size of arrays or tuples after creation?

---

No. Both arrays and tuples have fixed size determined at compile time. You cannot add or remove elements.

```rust
let mut arr = [1, 2, 3];
arr.push(4);  // ❌ Error: no push method
```


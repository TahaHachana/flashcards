## Borrowing Individual Struct Fields

Can you borrow multiple fields of a struct mutably?

---

Yes. Different fields are independent data, so borrowing them separately is safe.

```rust
let x_ref = &mut point.x;
let y_ref = &mut point.y;  // ✅ OK
```


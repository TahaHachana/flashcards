## Cannot Borrow Whole While Field Borrowed

Can you borrow an entire struct while one of its fields is already borrowed?

---

No. Borrowing the whole struct would provide access to the already-borrowed field.

```rust
let x_ref = &mut point.x;
let point_ref = &point;  // ❌ Error
```


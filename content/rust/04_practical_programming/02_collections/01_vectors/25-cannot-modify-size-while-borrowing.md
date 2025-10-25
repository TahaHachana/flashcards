## Cannot Modify Size While Borrowing

Why does this fail to compile?
```rust
let mut vec = vec![1, 2, 3];
for num in &vec {
    vec.push(*num * 2);  // ERROR!
}
```

---

The for loop borrows `vec` immutably (`&vec`). While borrowed, you cannot modify it with `.push()` (requires `&mut self`). The borrow checker prevents this to avoid iterator invalidation. Solution: collect changes in a separate vector first.


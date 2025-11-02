## Borrowing Rules vs Lifetime Issues

How do you distinguish between a borrowing rule violation and a lifetime issue?

---

Borrowing rules are about simultaneous access (can't have `&mut` and `&` at once, or two `&mut`). Lifetime issues are about validity duration (references outliving data). Example of borrowing issue (not lifetime):
```rust
fn bad(v: &mut Vec<i32>) -> (&mut i32, &mut i32) {
    (&mut v[0], &mut v[1])  // Can't have two &mut to same Vec!
}
```
This fails borrowing rules regardless of lifetimes.


## Vector as Function Parameter

What are three ways to pass a vector to a function, and when should you use each?

---

```rust
fn consume(v: Vec<i32>) {}      // Takes ownership
fn borrow(v: &Vec<i32>) {}      // Borrows immutably
fn modify(v: &mut Vec<i32>) {}  // Borrows mutably
```
Use owned when function needs to own/consume it; `&` for read-only; `&mut` for modification.


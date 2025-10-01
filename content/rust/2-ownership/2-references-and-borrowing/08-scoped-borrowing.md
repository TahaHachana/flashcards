## Scoped Borrowing

How can you reuse a mutable reference after another one?

---

Place the first borrow in a smaller scope so it ends before the next one begins.

```rust
let mut s = String::from("hello");
{
    let r1 = &mut s;
} // r1 is dropped here

let r2 = &mut s; // valid
```


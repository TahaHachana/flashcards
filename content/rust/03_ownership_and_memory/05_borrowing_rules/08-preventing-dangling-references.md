## Preventing Dangling References

How does the borrow checker prevent dangling references?

---

Tracks lifetimes and ensures references can't outlive the data they point to.

```rust
let r;
{
    let x = 5;
    r = &x;  // ❌ Error: x doesn't live long enough
}
// x dropped, r would be dangling
```


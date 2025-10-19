## Passing Copy Types to Functions

Should you pass Copy types by value or reference?

---

By value freely. Copying is cheap and the caller keeps the original.

```rust
fn distance(p1: Point, p2: Point) -> f64 {
    // p1, p2 are copies
}
```


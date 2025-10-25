## Data Race Prevention

How does the borrow checker prevent data races?

---

Enforces that only one mutable reference exists at a time. Multiple mutable references trying to modify simultaneously would cause data races.

```rust
let r1 = &mut counter;
let r2 = &mut counter;  // ❌ Prevents data race
```


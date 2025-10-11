## Integer Overflow Behavior

How does Rust handle integer overflow in debug vs release mode?

---

Debug mode: panics on overflow. Release mode: wraps around. Use methods like wrapping_add, checked_add, saturating_add, or overflowing_add for explicit control.

```rust
let x: u8 = 255;
let y = x.checked_add(1);  // Returns None
```


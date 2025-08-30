# Explicit Overflow Methods

What methods can you use to explicitly handle integer overflow?

---

- `wrapping_add()`: Wraps around on overflow
- `checked_add()`: Returns `None` on overflow
- `overflowing_add()`: Returns value and boolean indicating overflow
- `saturating_add()`: Clamps at min/max values
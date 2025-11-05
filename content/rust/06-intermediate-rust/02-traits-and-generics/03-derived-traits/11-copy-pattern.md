## Copy Type Derive Pattern

What is the typical derive pattern for small, Copy types?

---

```rust
#[derive(Debug, Copy, Clone, PartialEq, Eq)]
struct Color {
    r: u8,
    g: u8,
    b: u8,
}
```

**When to use**: Small types (typically ≤16 bytes) with no heap allocations. All fields must be `Copy`.

Remember: `Copy` always requires `Clone` to be derived together.


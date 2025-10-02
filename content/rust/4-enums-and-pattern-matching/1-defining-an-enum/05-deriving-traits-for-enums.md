## Deriving Traits For Enums

How can you automatically add traits like `Debug` or `Clone` to an enum?

---

Use the `#[derive]` attribute:

```rust
#[derive(Debug, Clone, PartialEq, Eq)]
enum Mode {
    Normal,
    Insert,
    Visual,
}
```


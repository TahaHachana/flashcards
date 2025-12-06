## The DerefMut Trait Definition

What is the `DerefMut` trait signature, and what's the relationship between `DerefMut` and `Deref`?

---

```rust
pub trait DerefMut: Deref {
    fn deref_mut(&mut self) -> &mut Self::Target;
}
```

**Key points:**
- `DerefMut: Deref` means `DerefMut` requires `Deref` to be implemented first
- Uses the same `Target` type from `Deref` (no new associated type needed)
- Takes `&mut self` instead of `&self`
- Returns `&mut Self::Target` instead of `&Self::Target`

**Relationship:** You cannot implement `DerefMut` without first implementing `Deref`. The `Target` type is shared between both traits.

Example:
```rust
impl Deref for MyType {
    type Target = u8;
    fn deref(&self) -> &u8 { &self.0 }
}

impl DerefMut for MyType {
    // No type Target needed - inherited from Deref
    fn deref_mut(&mut self) -> &mut u8 { &mut self.0 }
}
```


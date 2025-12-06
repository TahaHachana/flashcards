## The Deref Trait Definition

What is the `Deref` trait signature, and what does each part mean?

---

```rust
pub trait Deref {
    type Target: ?Sized;
    fn deref(&self) -> &Self::Target;
}
```

**Components:**
- `type Target`: Associated type - the type that `&Self` will dereference to
- `?Sized`: The target doesn't need a known size at compile time
- `fn deref(&self)`: Takes `&self` and returns `&Self::Target`

**Key insight:** `deref()` returns a **reference** to the target, not the target itself. This is crucial for maintaining borrow checking rules.

Example:
```rust
impl Deref for Box<T> {
    type Target = T;
    fn deref(&self) -> &T { /* ... */ }
}
```


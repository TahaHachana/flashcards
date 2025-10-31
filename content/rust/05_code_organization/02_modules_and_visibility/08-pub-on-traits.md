## Pub on Traits - All Methods Public

What happens when you mark a trait as `pub`?

---

**Rule**: When a trait is `pub`, **all its methods automatically become public**.

**Example**:
```rust
pub trait Drawable {
    fn draw(&self);    // Automatically public
    fn erase(&self);   // Automatically public
}
```

**Rationale**: Traits define shared behavior. If a trait is public, all its methods need to be accessible for others to:
- Implement the trait on their types
- Call the methods through the trait

**You can't have private methods in a public trait** - it wouldn't make sense.


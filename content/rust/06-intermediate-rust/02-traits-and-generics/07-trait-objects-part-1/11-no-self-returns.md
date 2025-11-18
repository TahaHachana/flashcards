## Object Safety Rule 1 - No Self Returns

Why can't object-safe trait methods return `Self`?

---

Returning `Self` is not object-safe because the compiler doesn't know the size of `Self` with trait objects:

```rust
// ❌ NOT object-safe
trait Cloneable {
    fn clone_self(&self) -> Self;
}

// Error: cannot be made into an object
let obj: Box<dyn Cloneable> = /* ... */;
```

**Solution**: Return `Box<dyn Trait>` instead:
```rust
// ✅ Object-safe
trait Cloneable {
    fn clone_box(&self) -> Box<dyn Cloneable>;
}
```

With trait objects, `Self` could be any size, but the return type must have a known size.


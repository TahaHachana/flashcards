## Object Safety Rule 3 - Associated Functions

Why can't object-safe traits have associated functions (functions without `self`)?

---

Associated functions without `self` are typically not object-safe because there's no instance to call them on:

```rust
// ❌ NOT object-safe
trait Factory {
    fn create() -> Self;
}

// Error: cannot be made into an object
let obj: Box<dyn Factory> = /* ... */;
```

**Why**: You'd call it as `Factory::create()`, but with a trait object, which concrete type should be created? The trait object doesn't know.

**Exception**: Associated functions that don't involve `Self` can be object-safe if they have a `where Self: Sized` bound.


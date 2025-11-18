## Checking Object Safety

How do you know if a trait is object-safe?

---

The compiler will tell you when you try to use a non-object-safe trait as a trait object:

```rust
trait NotObjectSafe {
    fn method<T>(&self);  // Generic method
}

let x: &dyn NotObjectSafe = &value;
// Error: the trait `NotObjectSafe` cannot be made into an object
```

**Object-safe traits**:
- All methods take `&self`, `&mut self`, or `self`
- No generic methods
- No methods returning `Self` (except special cases)
- No associated functions without `self`

If unsure, try creating a trait object - the compiler will guide you.


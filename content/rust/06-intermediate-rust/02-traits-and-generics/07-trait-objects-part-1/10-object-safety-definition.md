## What Is Object Safety?

What does it mean for a trait to be "object-safe"?

---

A trait is **object-safe** if it can be used as a trait object. Not all traits can be trait objects - they must follow certain rules that allow dynamic dispatch.

**Object-safe traits** can be used as:
```rust
Box<dyn Trait>
&dyn Trait
&mut dyn Trait
```

**Not object-safe traits** cannot be used this way and will cause a compiler error.

The compiler enforces these rules because dynamic dispatch requires certain guarantees about how methods are called.


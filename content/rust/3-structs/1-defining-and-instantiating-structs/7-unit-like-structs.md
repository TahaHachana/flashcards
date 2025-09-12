# Unit-Like Structs

What is a unit-like struct and when would you use it?

---

A unit-like struct is a struct with no fields. It behaves like the unit type `()` in terms of stored data (it occupies zero bytes) but has its own distinct type name. These are useful for:
- Marker / tag types (to convey intent or restrict APIs)
- Implementing traits where no data is required
- Phantom types (often combined with `PhantomData<T>`)
- Zero-cost abstractions (no runtime footprint)

```rust
// Definition: no braces with fields — just the name and a semicolon.
struct AlwaysEqual;

// Use just by naming it (instantiation is trivial).
let subject = AlwaysEqual;

// Implement a trait even without data.
use std::fmt;
impl fmt::Display for AlwaysEqual {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "<AlwaysEqual>")
    }
}
println!("{}", subject);
```

Key points:
- Zero-sized type (ZST): the compiler may optimize away its storage.
- Distinct from the unit value `()`, even though both store no data.
- Great for signaling behavior or capability via the type system.
- Often appears in advanced patterns (stateless services, type-state encodings, trait impl anchors).
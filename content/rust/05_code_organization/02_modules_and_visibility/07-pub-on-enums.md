## Pub on Enums - All Variants Public

What happens when you mark an enum as `pub`, and why?

---

**Rule**: When an enum is `pub`, **all its variants automatically become public**.

**Example**:
```rust
pub enum TrafficLight {
    Red,      // Automatically public
    Yellow,   // Automatically public
    Green,    // Automatically public
}
```

**Rationale**: Enums are about choosing between variants. If the enum is public, users need to see all variants to make a choice. Having private variants in a public enum wouldn't make sense.

**Same applies to data in variants** - it's all accessible if the enum is public.


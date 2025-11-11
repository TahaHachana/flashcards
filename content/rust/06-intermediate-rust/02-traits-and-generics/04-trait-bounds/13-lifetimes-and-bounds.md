## Trait Bounds with Lifetimes

How do you combine lifetime parameters with trait bounds?

---

Lifetimes come first, then trait bounds with `where`:

```rust
fn longest<'a, T>(x: &'a T, y: &'a T) -> &'a T
where
    T: PartialOrd,
{
    if x > y { x } else { y }
}
```

**Pattern**:

1. Declare lifetime parameters: `<'a>`
2. Declare type parameters: `<'a, T>`
3. Add trait bounds: `where T: TraitName`

Lifetimes and trait bounds serve different purposes and work together.


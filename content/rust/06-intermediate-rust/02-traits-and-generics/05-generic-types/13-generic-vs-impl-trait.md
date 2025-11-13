## Generic vs impl Trait Difference

What's the key difference between using generics and `impl Trait` for multiple parameters?

---

**Generic `<T>`**: All parameters must be the same type
**`impl Trait`**: Each parameter can be a different type

```rust
// ❌ Different types with impl Trait
fn compare(a: impl PartialOrd, b: impl PartialOrd) -> bool {
    a > b  // Error: might be comparing different types!
}

// ✅ Same type with generic
fn compare<T: PartialOrd>(a: T, b: T) -> bool {
    a > b  // Works: both are definitely type T
}
```

Use explicit generics when parameters must be the same type.


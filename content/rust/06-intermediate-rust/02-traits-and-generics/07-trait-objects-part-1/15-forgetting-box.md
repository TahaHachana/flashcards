## Forgetting Box Error

What error do you get if you forget to use `Box` with a trait object?

---

```rust
// ❌ WRONG
fn returns_trait() -> dyn Display {
    42
}
// Error: doesn't have a size known at compile-time
```

**Solution**: Use a pointer type:
```rust
// ✅ Boxed (owned)
fn returns_trait() -> Box<dyn Display> {
    Box::new(42)
}

// ✅ Reference (borrowed)
fn returns_trait_ref() -> &'static dyn Display {
    &42
}
```

Trait objects must be behind a pointer because their size is unknown at compile time.


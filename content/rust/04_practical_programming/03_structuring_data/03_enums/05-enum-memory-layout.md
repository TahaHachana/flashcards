## Enum Memory Layout

How is an enum's size determined in memory, and what's the implication for variants with different sizes?

---

Enum size = **largest variant's size + discriminant (tag)**

```rust
enum Example {
    Small(u8),           // 1 byte
    Large([u8; 100]),    // 100 bytes
}
// Size of Example = 100+ bytes for ALL instances
```

**Implication**: Even if you store `Example::Small`, it takes up 100+ bytes because the enum must be sized for its largest variant.

**Solution for large variants**: Use `Box` to store large data on the heap:
```rust
enum Example {
    Small(u8),
    Large(Box<[u8; 100]>),  // Now just a pointer
}
// Small variants now only take a few bytes
```

Avoid enums with vastly different-sized variants if you'll have many instances.


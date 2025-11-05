## Complete Derive Pattern

What is the "complete" derive pattern for maximum functionality?

---

```rust
#[derive(Debug, Clone, PartialEq, Eq, Hash, PartialOrd, Ord, Default)]
struct CompleteType {
    id: u64,
    name: String,
}
```

This gives you:
- Debug printing
- Cloning
- Equality comparison
- Ordering comparison
- Hashing (HashMap keys)
- Default values

Use for data container types that need all standard operations.


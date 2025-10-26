## Unit Structs

What are unit structs and what are three common use cases for them?

---

Unit structs have no fields at all:

```rust
struct AlwaysEqual;
let subject = AlwaysEqual;
```

**Three common use cases**:
1. **Implementing traits** without storing data
2. **Marker types** for type-level programming
3. **State machines** where some states carry no data

Unit structs are zero-sized types (ZSTs) that take up no memory but provide type distinction at compile time.


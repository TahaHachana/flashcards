## Trait Object Size

What is the size of a trait object pointer, and what information does it contain?

---

A trait object pointer (like `Box<dyn Trait>` or `&dyn Trait`) is a **fat pointer** containing two pointers (16 bytes on 64-bit systems):

1. **Data pointer**: Points to the actual value
2. **Vtable pointer**: Points to a table of function pointers for the trait methods

```rust
// Box<dyn Trait>: 16 bytes (2 pointers)
// - Pointer to heap data
// - Pointer to vtable

// &dyn Trait: 16 bytes (2 pointers)
// - Pointer to data
// - Pointer to vtable
```

The vtable enables dynamic dispatch - it tells the program which concrete method to call at runtime.


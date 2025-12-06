## Smart Pointer Comparison Table

Compare regular references and smart pointers across key features: ownership, cleanup, metadata, size, and heap allocation.

---

| Feature | Regular Reference | Smart Pointer |
|---------|------------------|---------------|
| **Ownership** | Borrows only | Owns the data |
| **Cleanup** | No cleanup needed | Automatic cleanup (Drop) |
| **Metadata** | None | Often includes extra info |
| **Size** | Pointer size | Pointer size (+ possible inline metadata) |
| **Dereferencing** | `*` operator | `*` operator (via Deref trait) |
| **Heap allocation** | Points anywhere | Often manages heap data |

Example showing ownership difference:
```rust
let value = 42;
let ref1 = &value;  // Borrows
// value still owned by original binding

let boxed = Box::new(42);  // Owns
// Box owns the 42, original value was moved
```


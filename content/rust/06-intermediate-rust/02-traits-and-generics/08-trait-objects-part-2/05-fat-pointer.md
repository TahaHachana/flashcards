## Fat Pointer Structure

What is a fat pointer and what does a trait object pointer contain?

---

A trait object pointer is a **fat pointer** containing two pointers (16 bytes on 64-bit):

1. **Data pointer** - Points to the actual value
2. **Vtable pointer** - Points to the table of function pointers

```rust
// Conceptual representation
struct TraitObject {
    data: *const (),      // Where the actual data is
    vtable: *const Vtable, // How to call methods on it
}

// Examples:
Box<dyn Trait>  // 16 bytes: data ptr + vtable ptr
&dyn Trait      // 16 bytes: data ptr + vtable ptr
```

This is why trait objects are "fat" - they're twice the size of a regular pointer.


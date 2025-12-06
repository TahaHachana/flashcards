## Key Smart Pointer Trinity

What is the "trinity" that makes smart pointers "smart"? Explain how each component contributes.

---

The smart pointer trinity: **Ownership + Metadata + Deref**

**1. Ownership:**
- Smart pointers own their data
- Responsible for cleanup when dropped
- Enable transfer of ownership without copying data

**2. Metadata:**
- Extra information about the data
- Examples: length, capacity (Vec), reference count (Rc), borrow state (RefCell)
- Enables functionality beyond simple indirection

**3. Deref:**
- Implement `Deref` trait for `*` operator
- Enable deref coercion for ergonomic use
- Allow treating smart pointer "like" its inner type

**Together they provide:**
```rust
let vec = vec![1, 2, 3];
// Ownership: vec owns the data
// Metadata: tracks length and capacity  
// Deref: can treat &Vec like &[i32]
let slice: &[i32] = &vec;  // Deref coercion
```

This trinity is what makes a pointer "smart" versus just being a raw pointer.


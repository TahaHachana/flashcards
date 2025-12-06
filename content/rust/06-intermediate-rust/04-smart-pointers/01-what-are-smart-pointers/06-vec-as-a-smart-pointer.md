## Vec as a Smart Pointer

How is `Vec<T>` a smart pointer to `[T]`? Explain its ownership, metadata, and deref properties.

---

`Vec<T>` is a smart pointer with:

**Ownership**: Owns the array data on the heap

**Metadata**:
- Length (number of elements currently stored)
- Capacity (allocated space for elements)

**Deref**: Implements `Deref<Target = [T]>`, allowing it to act like `&[T]`

Example:
```rust
let v = vec![1, 2, 3];
let slice: &[i32] = &v;  // Deref coercion to &[i32]
println!("Length: {}", v.len());     // Metadata
println!("Capacity: {}", v.capacity()); // Metadata
```

This is why you can pass `&Vec<T>` to functions expecting `&[T]`.


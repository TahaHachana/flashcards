## String as a Smart Pointer

How is `String` a smart pointer to `str`? Explain its ownership, metadata, and deref properties.

---

`String` is a smart pointer with:

**Ownership**: Owns the string data on the heap

**Metadata**: 
- Length (number of bytes currently used)
- Capacity (allocated space)

**Deref**: Implements `Deref<Target = str>`, allowing it to act like `&str`

Example:
```rust
let s = String::from("hello");
let s_ref: &str = &s;  // Deref coercion to &str
println!("Length: {}", s.len());     // Metadata
println!("Capacity: {}", s.capacity()); // Metadata
```

This is why you can pass `&String` to functions expecting `&str`.


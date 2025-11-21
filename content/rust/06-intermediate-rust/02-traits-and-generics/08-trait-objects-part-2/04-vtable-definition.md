## What Is a Vtable?

What is a vtable (virtual function table) and how does it enable dynamic dispatch?

---

A **vtable** is a table of function pointers used for dynamic dispatch. It contains pointers to the concrete implementations of trait methods.

**Structure** (conceptual):
```rust
struct Vtable {
    destructor: fn(*const ()),
    size: usize,
    align: usize,
    method1: fn(*const ()),  // Pointer to actual implementation
    method2: fn(*const ()),
    // ... one entry per trait method
}
```

**How it works**:
1. Trait object stores pointer to data + pointer to vtable
2. When method called: follow vtable pointer
3. Find method's function pointer in vtable
4. Call that function with data pointer

This extra indirection is the source of dynamic dispatch overhead.


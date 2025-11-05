## Why Copy Has Restrictions

Why can't `String` implement `Copy`, but `i32` can?

---

`Copy` is only for types that can be safely duplicated by simply copying bits (stack-only data). 

**`i32` can be Copy**: It's just 4 bytes on the stack. Copying the bits creates a valid duplicate.

**`String` cannot be Copy**: It contains a pointer to heap data. If you copied the bits, you'd have two pointers to the same heap memory, leading to double-free errors when both are dropped.

Only types with no heap allocations and no resource ownership can be `Copy`.


## Box Size and Memory Layout

What is the size of `Box<T>` vs `Box<[T]>`, and why the difference? Illustrate the memory layout.

---

**Sizes:**
```rust
use std::mem::size_of;

size_of::<Box<i32>>()          // 8 bytes
size_of::<Box<[i32; 100]>>()   // 8 bytes
size_of::<Box<[i32]>>()        // 16 bytes (!)
```

**Why the difference?**
- `Box<T>`: Just stores pointer to heap data (8 bytes)
- `Box<[T]>`: Stores pointer + length, because slice can be any size (16 bytes)

**Memory Layout:**
```
Box<T>:
Stack                    Heap
┌──────────┐            ┌──────────┐
│  Box<T>  │───────────▶│    T     │
│ (8 bytes)│            │  (data)  │
└──────────┘            └──────────┘

Box<[T]>:
Stack                    Heap
┌──────────┐            ┌──────────┐
│ pointer  │───────────▶│   [T]    │
│ length   │            │  (data)  │
│(16 bytes)│            └──────────┘
└──────────┘
```

**Key:** Fixed-size types need only pointer; dynamically-sized types need pointer + metadata.


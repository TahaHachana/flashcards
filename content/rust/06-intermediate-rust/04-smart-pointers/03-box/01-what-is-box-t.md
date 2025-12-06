## What is Box<T>?

What is `Box<T>` and what are its key characteristics?

---

`Box<T>` is Rust's most fundamental smart pointer that provides heap allocation. When you wrap a value in a `Box`, the value moves from the stack to the heap, while the `Box` itself (just a pointer) stays on the stack.

**Key characteristics:**
- Allocates data on the heap
- Has a known, fixed size (pointer-sized, typically 8 bytes)
- Owns the data it points to
- Automatically deallocates when dropped
- Zero runtime overhead (no reference counting)

**Example:**
```rust
let boxed = Box::new(5);  // 5 is on heap, pointer on stack
let value = *boxed;       // Access with *
```

Think of `Box` as saying: "Put this data on the heap and give me a pointer to it."


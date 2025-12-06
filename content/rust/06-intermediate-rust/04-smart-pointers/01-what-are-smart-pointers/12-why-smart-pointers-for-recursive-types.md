## Why Smart Pointers for Recursive Types

Why are smart pointers (like `Box`) necessary for recursive types? Explain with an example.

---

The compiler needs to know the size of every type at compile time. Recursive types have potentially infinite size, which the compiler cannot determine.

**Problem without Box:**
```rust
// Error: recursive type has infinite size
struct Node {
    value: i32,
    next: Option<Node>,  // Could be infinitely nested
}
```

**Solution with Box:**
```rust
struct Node {
    value: i32,
    next: Option<Box<Node>>,  // Box always has pointer size
}
```

`Box` works because:
- Its size is known (always pointer-sized)
- The actual data is on the heap
- The compiler only needs to know the pointer size, not the full structure's size

This allows recursive structures like linked lists, trees, and graphs.


## Stack vs Heap Memory

Compare stack and heap memory, and explain when you'd use `Box` to move data from stack to heap.

---

**Stack:**
- Fast allocation/deallocation (just move a pointer)
- Limited size (typically 2-8MB)
- Automatic cleanup
- LIFO (Last In, First Out) order

**Heap:**
- Slower allocation (need to find free space)
- Large size available
- Manual cleanup (Rust automates via `Drop`)
- No particular order

**When to use Box:**
```rust
// ❌ Risk of stack overflow
// let large = [0; 1_000_000];

// ✅ Safe on heap
let large = Box::new([0; 1_000_000]);
```

**Use Box when:**
- Data is too large for stack (>1MB)
- You need recursive types
- You want to control where data lives
- You're transferring ownership of large data

Stack is faster but limited; heap (via Box) is slower but virtually unlimited.


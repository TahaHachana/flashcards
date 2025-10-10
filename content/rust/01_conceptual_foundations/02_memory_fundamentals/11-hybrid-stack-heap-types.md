## Hybrid Stack-Heap Types

How do types like String and Vec<T> use both stack and heap?

---

They store metadata (pointer, length, capacity) on the stack as a small handle, while the actual data lives on the heap. The stack part points to the heap part.

```rust
let s = String::from("hello");
// Stack: { ptr, len: 5, capacity: 5 }
// Heap: ['h', 'e', 'l', 'l', 'o']
```


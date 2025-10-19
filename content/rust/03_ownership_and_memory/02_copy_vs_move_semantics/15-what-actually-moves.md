## What Actually Moves

When ownership moves for heap-allocated types, what gets copied?

---

Only the stack portion (pointer, length, capacity, etc.). The heap data isn't duplicated. The old variable is marked invalid to prevent double-free.

```rust
// Stack: [ptr, len, cap] copied
// Heap: same data, not duplicated
// s1: marked invalid
```


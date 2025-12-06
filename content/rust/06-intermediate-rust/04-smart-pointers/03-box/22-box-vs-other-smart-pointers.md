## Box vs Other Smart Pointers

Compare `Box<T>` with `Rc<T>` and `Arc<T>`. When would you choose each?

---

**Box<T>:**
- Single ownership
- Heap allocation
- No runtime overhead (besides allocation)
- Not shareable
```rust
let b = Box::new(5);
// Cannot have multiple owners
```

**Rc<T>:** (next topic in roadmap)
- Multiple ownership (single-threaded)
- Reference counting
- Small runtime overhead (increment/decrement)
- Shareable within one thread
```rust
let rc1 = Rc::new(5);
let rc2 = Rc::clone(&rc1);  // Both own the data
```

**Arc<T>:** (coming after Rc)
- Multiple ownership (multi-threaded)
- Atomic reference counting
- Larger runtime overhead (atomic operations)
- Shareable across threads
```rust
let arc1 = Arc::new(5);
let arc2 = Arc::clone(&arc1);  // Thread-safe
```

**Choose:**
- `Box`: Single owner, heap allocation
- `Rc`: Multiple owners, single thread
- `Arc`: Multiple owners, multiple threads


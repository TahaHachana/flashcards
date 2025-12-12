## RefCell and Mutex Overhead

Compare the runtime overhead of regular mutation, RefCell, and Mutex. What does each add?

---

**Operation costs:**

```markdown
| Operation      | Cost       | What's added              |
|----------------|------------|---------------------------|
| Regular &mut   | ~0ns       | Nothing (compile-time)    |
| RefCell        | ~5-10ns    | Runtime borrow check      |
| Mutex          | ~100-200ns | OS lock + atomics         |
```

**Comparison:**
```rust
// Regular mutation: ~0ns
let mut x = 5;
x += 1;

// RefCell: ~5-10ns per borrow
let x = RefCell::new(5);
*x.borrow_mut() += 1;

// Mutex: ~100-200ns per lock
let x = Mutex::new(5);
*x.lock().unwrap() += 1;
```

**What each adds:**

**RefCell:**
- Borrow state storage (1-2 bytes)
- Runtime borrow checking (~5-10 CPU cycles)
- Guard object creation (stack allocation)

**Mutex:**
- OS-level locking (~100ns)
- Context switch potential
- Cache synchronization
- Atomic operations

**Trade-off:**
- Regular `&mut`: Zero cost, compile-time safety, less flexible
- RefCell: Small cost, runtime safety, more flexible (single-threaded)
- Mutex: Larger cost, runtime safety, thread-safe

**When overhead matters:** Tight loops, low-latency systems, hot paths.


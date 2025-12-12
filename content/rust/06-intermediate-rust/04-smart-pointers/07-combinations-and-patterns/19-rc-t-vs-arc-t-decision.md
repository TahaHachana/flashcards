## Rc<T> vs Arc<T> Decision

What's the key question for deciding between `Rc` and `Arc`? What are the trade-offs?

---

**Key question: Will this data cross thread boundaries?**

**Use Rc when:**
- ✅ Guaranteed single-threaded
- ✅ UI applications (main thread only)
- ✅ Single-threaded game engines
- ✅ Need best performance (~20% faster than Arc)

**Use Arc when:**
- ✅ Data shared across threads
- ✅ Might add threading later
- ✅ Web servers, async code
- ✅ Safety over micro-optimization

**Trade-offs:**

```markdown
| Feature      | Rc                        | Arc                             |
|--------------|---------------------------|---------------------------------|
| Performance  | Faster (~60ns allocation) | Slower (~80ns allocation)       |
| Clone cost   | ~2-3 CPU cycles           | ~5-10 CPU cycles (atomic)       |
| Thread-safe  | No                        | Yes                             |
| Overhead     | Reference count           | Atomic reference count          |
| Traits       | No Send/Sync              | Send + Sync                     |
```

**Example:**
```rust
// Rc: single-threaded
let data = Rc::new(vec![1, 2, 3]);
// ❌ Can't send to thread

// Arc: multi-threaded
let data = Arc::new(vec![1, 2, 3]);
thread::spawn(move || {  // ✅ Can send to thread
    println!("{:?}", data);
});
```

**Rule:** Default to `Arc` if unsure. The performance difference is negligible in most code, and `Arc` gives you threading flexibility.


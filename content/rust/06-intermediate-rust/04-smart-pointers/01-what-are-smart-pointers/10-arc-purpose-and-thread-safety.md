## Arc Purpose and Thread Safety

What is `Arc<T>`, how does it differ from `Rc<T>`, and when should you use it?

---

`Arc<T>` (Atomic Reference Counted) is the thread-safe version of `Rc<T>`.

**Differences from `Rc<T>`:**
- Uses atomic operations for reference counting (thread-safe)
- Slightly slower than `Rc` due to atomic overhead
- Can be shared across threads
- Implements `Send` and `Sync` traits

**When to use:**
- When sharing data between multiple threads
- When you need multiple ownership in concurrent contexts
- Often combined with `Mutex<T>` for shared mutable state: `Arc<Mutex<T>>`

Example:
```rust
use std::sync::Arc;
use std::thread;

let shared = Arc::new(vec![1, 2, 3]);
let shared_clone = Arc::clone(&shared);

thread::spawn(move || {
    println!("{:?}", shared_clone);
});
```


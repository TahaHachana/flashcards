## What is Arc<T>?

What is `Arc<T>` and what are its key characteristics?

---

`Arc<T>` (Atomic Reference Counted) is the thread-safe version of `Rc<T>`. It enables **multiple ownership** of the same data across **multiple threads** using atomic operations for reference counting.

**Key characteristics:**
- Enables shared ownership across threads
- Thread-safe (atomic reference counting)
- Slightly slower than `Rc` (atomic operations overhead)
- Immutable by default (combine with `Mutex`/`RwLock` for mutation)
- Implements `Send` and `Sync` traits

**Example:**
```rust
use std::sync::Arc;
use std::thread;

let data = Arc::new(vec![1, 2, 3]);
let data_clone = Arc::clone(&data);

thread::spawn(move || {
    println!("{:?}", data_clone);  // Safe across threads!
});
```

Think of `Arc` as `Rc` but designed for multi-threaded programs - it's the safe way to share data between threads.


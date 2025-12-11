## Gotcha - RefCell is Not Thread-Safe

What happens if you try to use `RefCell` across threads? What's the error and solution?

---

**The problem:**
```rust
use std::cell::RefCell;
use std::thread;

let cell = RefCell::new(5);

// ❌ Won't compile
thread::spawn(move || {
    *cell.borrow_mut() = 10;
});
```

**Error:**
```
error[E0277]: `RefCell<i32>` cannot be sent between threads safely
   |
   = help: the trait `Send` is not implemented for `RefCell<i32>`
```

**Why?** RefCell uses non-atomic operations for borrow tracking, which isn't thread-safe.

**Solution: Use Mutex**
```rust
use std::sync::Mutex;
use std::thread;

let mutex = Mutex::new(5);

// ✅ Works! Mutex is thread-safe
thread::spawn(move || {
    *mutex.lock().unwrap() = 10;
});
```

**Comparison:**
```
Single-threaded interior mutability:
- RefCell: Runtime borrow checking, fast
- Cell: For Copy types, fastest

Multi-threaded interior mutability:
- Mutex: Thread-safe locking
- RwLock: Multiple readers, single writer
```

**Rule:** RefCell is for single-threaded code only. Use Mutex/RwLock for threads.


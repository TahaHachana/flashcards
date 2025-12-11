## Gotcha - Rc is Not Thread-Safe

What happens if you try to send `Rc` across threads? What's the error and solution?

---

**The problem:**
```rust
use std::rc::Rc;
use std::thread;

let data = Rc::new(vec![1, 2, 3]);

// ❌ This won't compile
thread::spawn(move || {
    println!("{:?}", data);
});
```

**Error:**
```
error[E0277]: `Rc<Vec<i32>>` cannot be sent between threads safely
   |
   = help: the trait `Send` is not implemented for `Rc<Vec<i32>>`
```

**Why?** `Rc` uses non-atomic reference counting (not thread-safe). Multiple threads could corrupt the counter.

**The solution: Use `Arc` (Atomic Reference Counted):**
```rust
use std::sync::Arc;
use std::thread;

let data = Arc::new(vec![1, 2, 3]);

// ✅ Works! Arc is thread-safe
thread::spawn(move || {
    println!("{:?}", data);
});
```

**Rule:** 
- Single thread? → `Rc`
- Multiple threads? → `Arc`

**Cost:** Arc is slightly slower due to atomic operations.


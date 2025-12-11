## Why Rc Fails with Threads

Why can't you use `Rc` with threads? What error does the compiler give?

---

`Rc` uses non-atomic reference counting, which isn't thread-safe. The compiler prevents sending `Rc` between threads.

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

**Why it's unsafe:**
If two threads increment/decrement the counter simultaneously, the count could become corrupted, leading to:
- Memory leaks (data never freed)
- Use-after-free (data freed while still in use)
- Data races

**Solution:** Use `Arc` which has atomic operations that prevent these issues.


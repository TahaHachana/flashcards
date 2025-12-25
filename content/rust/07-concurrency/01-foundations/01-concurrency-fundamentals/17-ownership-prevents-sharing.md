## Ownership Prevents Sharing

Why does this code fail to compile, and what is Rust preventing?
```rust
let mut data = vec![1, 2, 3];
thread::spawn(|| { data.push(4); });
data.push(5);
```

---

This fails because the closure might outlive the current function but tries to borrow `data`. Both the spawned thread and main thread would have access to `data` and could mutate it simultaneously, creating a data race. Rust's compiler prevents this at compile time, enforcing that only one thread can own mutable data. You must use `move` to transfer ownership or use synchronization primitives like `Arc<Mutex<T>>`.


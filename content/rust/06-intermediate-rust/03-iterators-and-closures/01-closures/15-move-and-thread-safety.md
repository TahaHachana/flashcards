## Move and Thread Safety

Why is the `move` keyword required for closures in threads? What would happen without it?

---

Threads require closures to own their data because the spawned thread may outlive the scope where data was created.

**Without `move` (won't compile):**
```rust
let data = String::from("hello");
thread::spawn(|| println!("{}", data)); // ERROR
```

**Error:** The closure might outlive `data`, creating a dangling reference.

**With `move` (correct):**
```rust
let data = String::from("hello");
thread::spawn(move || println!("{}", data))
    .join()
    .unwrap();
```

**Why it's required:**
- Threads have independent lifetimes
- The spawning thread might end before the spawned thread
- `move` transfers ownership, ensuring data lives long enough
- This gives the closure `'static` lifetime

Thread spawn requires `FnOnce + Send + 'static`, and `move` helps satisfy the `'static` requirement.


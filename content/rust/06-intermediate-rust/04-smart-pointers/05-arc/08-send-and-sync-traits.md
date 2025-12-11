## Send and Sync Traits

Explain the `Send` and `Sync` traits. Which types implement them and why does it matter?

---

These marker traits determine thread safety:

**Send:** Type can be **transferred** between threads
```rust
// Can move ownership to another thread
thread::spawn(move || {
    // take ownership
});
```

**Sync:** Type can be **shared** between threads (via `&T`)
```rust
// Multiple threads can hold references
let reference = &data;
```

**Trait implementations:**

| Type | Send | Sync | Thread Safety |
|------|------|------|---------------|
| `i32` | Yes | Yes | Safe to send/share |
| `Rc<T>` | No | No | Not thread-safe |
| `Arc<T>` | Yes* | Yes* | Thread-safe |
| `Mutex<T>` | Yes* | Yes* | Provides thread-safe mutation |

*If T is Send/Sync

**Why it matters:**
```rust
// ❌ Rc doesn't implement Send
let rc = Rc::new(5);
thread::spawn(move || { });  // Error!

// ✅ Arc implements Send
let arc = Arc::new(5);
thread::spawn(move || { });  // Works!
```

The compiler uses these traits to prevent thread-unsafe code.


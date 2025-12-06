## Common Drop Use Cases

What are four common use cases for implementing the `Drop` trait?

---

**1. Releasing Resources:**
```rust
struct FileHandle {
    file: std::fs::File,
}

impl Drop for FileHandle {
    fn drop(&mut self) {
        println!("Closing file");
        // File automatically closed
    }
}
```

**2. Logging/Debugging:**
```rust
impl Drop for DebugDrop {
    fn drop(&mut self) {
        println!("Dropping: {}", self.name);
    }
}
```

**3. Reference Counting:**
```rust
// Rc<T> uses Drop to decrement reference count
// and free memory when count reaches 0
```

**4. Mutex Guards:**
```rust
// MutexGuard uses Drop to release the lock
// when the guard goes out of scope
```

Drop is essential for RAII - ensuring resources are cleaned up even if panics occur.


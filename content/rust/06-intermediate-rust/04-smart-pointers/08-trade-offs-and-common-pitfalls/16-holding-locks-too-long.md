## Holding Locks Too Long

What's the problem with holding Mutex locks too long? Show bad and good examples.

---

**The problem:**
```rust
// ❌ Bad: lock held during I/O
let mut guard = mutex.lock().unwrap();
guard.update();
write_to_disk(&guard);  // Slow! Other threads blocked
network_request(&guard);  // Very slow!
```

**Impact:**
- Reduces parallelism (other threads waiting)
- Increases contention
- Degrades performance
- Can cause timeouts

**Solution 1: Copy and release**
```rust
// ✅ Good: minimal lock time
let data_to_write = {
    let guard = mutex.lock().unwrap();
    guard.clone()
};  // Lock released

write_to_disk(&data_to_write);  // No lock held
```

**Solution 2: Batch operations**
```rust
// ❌ Bad: multiple lock acquisitions
for item in items {
    mutex.lock().unwrap().push(item);
}

// ✅ Good: single lock
{
    let mut guard = mutex.lock().unwrap();
    for item in items {
        guard.push(item);
    }
}
```

**Solution 3: Use RwLock for reads**
```rust
// If mostly reading, RwLock allows concurrent reads
let rwlock = Arc::new(RwLock::new(data));
let guard = rwlock.read().unwrap();  // Multiple readers OK
```

**Rule:** Lock for the absolute minimum time necessary.


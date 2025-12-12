## Preventing Deadlocks - Minimize Lock Duration

Why should you minimize lock duration, and how do you do it?

---

**Why minimize lock duration:**
- Reduces contention (other threads waiting)
- Decreases deadlock probability
- Improves parallelism
- Better performance

**❌ Bad: holding lock too long**
```rust
let guard = mutex.lock().unwrap();
expensive_computation();  // Lock held entire time!
use_data(&guard);
```

**Problems:**
- Other threads blocked during entire computation
- Increases chance of deadlock with other locks
- Reduces parallelism

**✅ Good: minimal lock time**
```rust
let data_copy = {
    let guard = mutex.lock().unwrap();
    guard.clone()
};  // Lock released immediately

expensive_computation();  // No lock held
use_data(&data_copy);
```

**Pattern:**
1. Lock
2. Copy what you need (quick)
3. Unlock
4. Do expensive work without lock

**Another example:**
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
}  // Lock released
```

**Rule:** Lock late, unlock early. Keep critical sections as short as possible.


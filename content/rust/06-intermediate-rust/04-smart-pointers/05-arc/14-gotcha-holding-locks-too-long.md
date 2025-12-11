## Gotcha - Holding Locks Too Long

What's the problem with holding Mutex locks too long, and how do you fix it?

---

**The problem:**
```rust
use std::sync::{Arc, Mutex};

// ❌ Bad: holds lock during expensive operation
let result = {
    let data = arc_mutex.lock().unwrap();
    expensive_operation(&data)  // Lock held entire time!
    // Other threads blocked during entire operation
};
```

**Why it's bad:**
- Lock held while doing slow work
- Other threads blocked unnecessarily
- Reduces parallelism
- Can cause performance bottlenecks

**Solution: Copy what you need, release lock**
```rust
// ✅ Good: minimal lock duration
let data_copy = {
    let data = arc_mutex.lock().unwrap();
    data.clone()  // Quick operation
};  // Lock released immediately

// Do expensive work without holding lock
let result = expensive_operation(&data_copy);
```

**Pattern:**
1. Lock
2. Copy/extract what you need (quickly)
3. Unlock (automatic when guard drops)
4. Do expensive work outside lock

**Alternative: explicit drop**
```rust
{
    let mut data = arc_mutex.lock().unwrap();
    data.some_quick_update();
    drop(data);  // Explicitly release lock
}
// Do other work
```

**Key insight:** Minimize time between `.lock()` and guard drop.


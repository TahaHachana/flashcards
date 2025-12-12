## Preventing Deadlocks - Consistent Lock Ordering

How does consistent lock ordering prevent deadlocks? Show the solution.

---

**The solution: Always lock in the same order**

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let mutex1 = Arc::new(Mutex::new(0));
    let mutex2 = Arc::new(Mutex::new(0));
    
    // Thread 1: Always lock mutex1 first, then mutex2
    let m1 = Arc::clone(&mutex1);
    let m2 = Arc::clone(&mutex2);
    thread::spawn(move || {
        let _g1 = m1.lock().unwrap();  // Lock 1 first
        let _g2 = m2.lock().unwrap();  // Then 2
        println!("Thread 1: got both locks");
    });
    
    // Thread 2: Same order - mutex1 first, then mutex2
    let m1 = Arc::clone(&mutex1);
    let m2 = Arc::clone(&mutex2);
    thread::spawn(move || {
        let _g1 = m1.lock().unwrap();  // Lock 1 first
        let _g2 = m2.lock().unwrap();  // Then 2
        println!("Thread 2: got both locks");
    });
    
    // No deadlock! Both threads follow same order
}
```

**Why it works:**
- Both threads try to lock mutex1 first
- One thread gets it, other waits
- First thread locks mutex2, completes, releases both
- Second thread then acquires both in order
- No circular waiting = no deadlock

**Pattern:**
```
Thread A: lock(1) → lock(2) → unlock(2) → unlock(1)
Thread B: lock(1) → lock(2) → unlock(2) → unlock(1)
✅ No deadlock
```

**Rule:** Establish lock ordering hierarchy and always follow it.


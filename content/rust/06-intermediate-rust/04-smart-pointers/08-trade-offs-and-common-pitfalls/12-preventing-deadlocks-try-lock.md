## Preventing Deadlocks - try_lock

How can `try_lock` prevent deadlocks? Show the pattern.

---

**Use try_lock to avoid blocking:**

```rust
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

fn acquire_both(m1: &Mutex<i32>, m2: &Mutex<i32>) {
    loop {
        // Try to lock first mutex
        let g1 = m1.try_lock();
        
        match g1 {
            Ok(guard1) => {
                // Got first lock, try second
                match m2.try_lock() {
                    Ok(guard2) => {
                        // Got both locks!
                        println!("Got both locks");
                        // Use guards...
                        break;
                    }
                    Err(_) => {
                        // Couldn't get second lock
                        // Release first and retry
                        drop(guard1);
                        thread::sleep(Duration::from_millis(10));
                    }
                }
            }
            Err(_) => {
                // Couldn't get first lock, retry
                thread::sleep(Duration::from_millis(10));
            }
        }
    }
}
```

**How it prevents deadlock:**
- `try_lock` doesn't block - returns immediately
- If can't get lock, back off and retry
- No circular waiting possible
- Eventually one thread gets both locks

**Pattern:**
1. Try to acquire all locks
2. If any fails, release all and retry
3. Back off before retry (avoid livelock)

**Trade-off:**
- ✅ No deadlocks
- ✅ More flexible
- ⚠️ More complex code
- ⚠️ Potential livelock (both keep retrying)

**Best use:** When you can't guarantee lock ordering.


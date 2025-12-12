## Arc<Mutex<T>> Pattern

What is `Arc<Mutex<T>>`, what does each layer provide, and when should you use it?

---

**What it provides:**
```
Arc<Mutex<T>>
│
├─ Arc: Multiple threads can share the same data (atomic ref counting)
│
└─ Mutex: Only one thread can access data at a time (mutual exclusion)
```

**Capabilities:**
- ✅ Multiple owners across threads
- ✅ Thread-safe mutation
- ✅ Prevents data races
- ⚠️ Higher overhead (atomics + OS locks)

**When to use:**
1. Multiple threads need to own the data
2. Data needs to be mutable
3. General-purpose thread-safe shared state
4. Writes and reads are roughly balanced

**Example:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter_clone = Arc::clone(&counter);
    
    let handle = thread::spawn(move || {
        for _ in 0..100 {
            *counter_clone.lock().unwrap() += 1;
        }
    });
    
    handles.push(handle);
}

for handle in handles {
    handle.join().unwrap();
}

println!("Result: {}", counter.lock().unwrap());  // 1000
```

**Common use cases:** Shared counters, thread-safe caches, connection pools, shared application state


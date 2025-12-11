## Arc<Mutex<T>> Complete Pattern

Explain the `Arc<Mutex<T>>` pattern with a counter example. What does each layer provide?

---

**Counter example:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];
    
    // Spawn 10 threads, each increments 10 times
    for _ in 0..10 {
        let counter_clone = Arc::clone(&counter);
        
        let handle = thread::spawn(move || {
            for _ in 0..10 {
                *counter_clone.lock().unwrap() += 1;
            }
        });
        
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
    
    println!("Result: {}", counter.lock().unwrap());  // 100
}
```

**Understanding the layers:**
```
Arc<Mutex<i32>>
│
├─ Arc: Enables sharing across threads (atomic ref counting)
│
└─ Mutex: Enables safe mutation (one thread at a time)
   │
   └─ i32: The actual data
```

**Each layer solves a problem:**
- `i32` alone: Can't share across threads
- `Arc<i32>`: Can share, but immutable
- `Arc<Mutex<i32>>`: Can share AND mutate safely ✓

Output is always `100` (predictable and safe).


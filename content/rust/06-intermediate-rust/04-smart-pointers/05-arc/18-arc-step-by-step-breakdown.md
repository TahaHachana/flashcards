## Arc Step-by-Step Breakdown

Break down what happens at each step when using `Arc<Mutex<T>>` across threads.

---

```rust
use std::sync::{Arc, Mutex};
use std::thread;

// 1. Create Arc<Mutex<T>>
let data = Arc::new(Mutex::new(0));
// Heap: RefCount=1, Data=Mutex(0)

// 2. Clone Arc for thread
let data_clone = Arc::clone(&data);
// Heap: RefCount=2 (atomic increment), same Mutex

// 3. Move into thread
thread::spawn(move || {
    // data_clone moved, data still usable in main
    
    // 4. Lock the mutex (blocks if already locked)
    let mut guard = data_clone.lock().unwrap();
    // MutexGuard holds exclusive access
    
    // 5. Mutate through guard
    *guard += 1;
    
    // 6. Guard dropped, mutex unlocked automatically
});  // data_clone dropped, RefCount decremented

// Main thread can still use data
println!("{}", data.lock().unwrap());
```

**What happens to counts:**
```
Initial:           RefCount=1
After clone:       RefCount=2
After thread move: RefCount=2 (ownership transferred)
After thread ends: RefCount=1 (decrement when dropped)
After main ends:   RefCount=0 → data freed
```

**Key insights:**
- Arc cloning is cheap (atomic counter update)
- Mutex locking can block (wait for unlock)
- Guard automatically unlocks on drop
- Data freed when last Arc dropped


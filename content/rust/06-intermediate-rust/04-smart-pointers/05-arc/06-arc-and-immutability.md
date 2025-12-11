## Arc and Immutability

Why can't you mutate data through `Arc` alone, and what's the solution?

---

**The problem:**
```rust
use std::sync::Arc;

let data = Arc::new(vec![1, 2, 3]);

// ❌ Cannot mutate through Arc
// data.push(4);  // Error!
```

**Why?** Multiple threads with mutable access would violate Rust's aliasing rules and cause data races.

**Solution: Arc<Mutex<T>>**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let mut handles = vec![];

for i in 0..5 {
    let data_clone = Arc::clone(&data);
    
    let handle = thread::spawn(move || {
        // Lock, mutate, automatically unlock
        data_clone.lock().unwrap().push(i);
    });
    
    handles.push(handle);
}

for handle in handles {
    handle.join().unwrap();
}

println!("{:?}", data.lock().unwrap());
```

**Pattern:** `Arc<Mutex<T>>` is the standard pattern for shared mutable state across threads.

Arc provides sharing, Mutex provides safe mutation.


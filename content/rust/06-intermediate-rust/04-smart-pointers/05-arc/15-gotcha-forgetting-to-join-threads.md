## Gotcha - Forgetting to Join Threads

What happens if you forget to join threads when using `Arc`, and how do you fix it?

---

**The problem:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let data = Arc::new(Mutex::new(0));
    
    for _ in 0..10 {
        let data_clone = Arc::clone(&data);
        thread::spawn(move || {
            *data_clone.lock().unwrap() += 1;
        });
    }
    
    // ⚠️ main() might end before threads finish!
    println!("{}", data.lock().unwrap());  // Might print 0-10
}
```

**What happens:**
- Threads spawned but not joined
- `main()` can exit while threads still running
- Program terminates, killing incomplete threads
- Unpredictable results

**Solution: Store handles and join**
```rust
fn main() {
    let data = Arc::new(Mutex::new(0));
    let mut handles = vec![];
    
    for _ in 0..10 {
        let data_clone = Arc::clone(&data);
        let handle = thread::spawn(move || {
            *data_clone.lock().unwrap() += 1;
        });
        handles.push(handle);  // Store handle
    }
    
    // Wait for all threads to complete
    for handle in handles {
        handle.join().unwrap();
    }
    
    println!("{}", data.lock().unwrap());  // Always prints 10
}
```

**Key insight:** Always join threads unless you specifically want detached threads.


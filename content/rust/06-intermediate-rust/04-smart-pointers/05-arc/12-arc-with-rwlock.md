## Arc with RwLock

When should you use `Arc<RwLock<T>>` instead of `Arc<Mutex<T>>`? Demonstrate the pattern.

---

**Use RwLock when:**
- Many readers
- Few writers
- Reads are more common than writes

**Pattern:**
```rust
use std::sync::{Arc, RwLock};
use std::thread;

fn main() {
    let data = Arc::new(RwLock::new(vec![1, 2, 3]));
    let mut handles = vec![];
    
    // Many readers (can read concurrently)
    for i in 0..5 {
        let data_clone = Arc::clone(&data);
        let handle = thread::spawn(move || {
            let read_guard = data_clone.read().unwrap();
            println!("Reader {}: {:?}", i, *read_guard);
            // Multiple readers can hold locks simultaneously
        });
        handles.push(handle);
    }
    
    // One writer (exclusive access)
    let data_clone = Arc::clone(&data);
    let handle = thread::spawn(move || {
        let mut write_guard = data_clone.write().unwrap();
        write_guard.push(4);
        println!("Writer: modified data");
        // Only one writer at a time
    });
    handles.push(handle);
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**RwLock rules:**
- Multiple `.read()` locks simultaneously: ✅
- One `.write()` lock at a time: ✅
- `.write()` blocks all `.read()` and other `.write()`: ✅

**Benefit:** Better performance when reads >> writes.


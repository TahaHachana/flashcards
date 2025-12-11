## Basic Arc Usage with Threads

Demonstrate the pattern for sharing data across multiple threads using `Arc`.

---

```rust
use std::sync::Arc;
use std::thread;

fn main() {
    // 1. Create Arc
    let data = Arc::new(vec![1, 2, 3]);
    let mut handles = vec![];
    
    // 2. Spawn multiple threads
    for i in 0..10 {
        // 3. Clone Arc for each thread
        let data_clone = Arc::clone(&data);
        
        // 4. Move clone into thread
        let handle = thread::spawn(move || {
            println!("Thread {}: {:?}", i, data_clone);
        });
        
        handles.push(handle);
    }
    
    // 5. Wait for all threads
    for handle in handles {
        handle.join().unwrap();
    }
    
    println!("Strong count: {}", Arc::strong_count(&data));  // 1
}
```

**Pattern:**
1. Create `Arc` in main thread
2. Clone `Arc` for each thread (cheap - just increments atomic counter)
3. Move clone into thread
4. Each thread safely accesses shared data
5. Join threads to wait for completion

**Key insight:** Original `data` is still usable in main thread after spawning threads.


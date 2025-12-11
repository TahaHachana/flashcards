## Parallel Data Processing Pattern

Show how to use `Arc<Mutex<T>>` for parallel data processing with shared results.

---

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let data = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let results = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];
    
    // Split work across threads
    for chunk in data.chunks(3) {
        let results_clone = Arc::clone(&results);
        let chunk_vec = chunk.to_vec();
        
        let handle = thread::spawn(move || {
            // Process chunk
            let sum: i32 = chunk_vec.iter().sum();
            
            // Store result (safe with Mutex)
            results_clone.lock().unwrap().push(sum);
        });
        
        handles.push(handle);
    }
    
    // Wait for all threads
    for handle in handles {
        handle.join().unwrap();
    }
    
    println!("Results: {:?}", results.lock().unwrap());
}
```

**Pattern:**
- Each thread processes a portion of data
- Results stored in shared `Arc<Mutex<Vec>>`
- Mutex ensures safe concurrent writes
- Main thread collects all results


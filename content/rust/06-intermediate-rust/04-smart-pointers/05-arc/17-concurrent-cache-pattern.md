## Concurrent Cache Pattern

Implement a concurrent cache using `Arc<Mutex<HashMap>>` that multiple threads can read from and write to.

---

```rust
use std::sync::{Arc, Mutex};
use std::collections::HashMap;
use std::thread;

type Cache = Arc<Mutex<HashMap<String, String>>>;

fn get_or_compute(cache: Cache, key: String) -> String {
    // Check cache (short lock)
    {
        let cache_read = cache.lock().unwrap();
        if let Some(value) = cache_read.get(&key) {
            return value.clone();
        }
    }  // Lock released
    
    // Compute (expensive, no lock held)
    let value = format!("computed_{}", key);
    
    // Update cache (short lock)
    cache.lock().unwrap().insert(key.clone(), value.clone());
    
    value
}

fn main() {
    let cache: Cache = Arc::new(Mutex::new(HashMap::new()));
    let mut handles = vec![];
    
    for i in 0..10 {
        let cache_clone = Arc::clone(&cache);
        let key = format!("key_{}", i % 3);  // Some keys repeated
        
        let handle = thread::spawn(move || {
            let value = get_or_compute(cache_clone, key);
            println!("Got: {}", value);
        });
        
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**Pattern benefits:**
- Thread-safe concurrent access
- Lock held for minimal time
- Expensive computation outside lock
- Cache shared across all threads


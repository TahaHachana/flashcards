## Thread Pool with Shared Config Pattern

Demonstrate using `Arc` to share configuration across a thread pool.

---

```rust
use std::sync::Arc;
use std::thread;

struct Config {
    thread_count: usize,
    timeout_ms: u64,
    api_key: String,
}

fn worker(id: usize, config: Arc<Config>) {
    println!("Worker {}: timeout = {}ms", 
             id, config.timeout_ms);
    // Worker uses config...
}

fn main() {
    // Create config once
    let config = Arc::new(Config {
        thread_count: 4,
        timeout_ms: 5000,
        api_key: "secret".to_string(),
    });
    
    let mut handles = vec![];
    
    // Share config across all workers
    for i in 0..config.thread_count {
        let config_clone = Arc::clone(&config);
        let handle = thread::spawn(move || {
            worker(i, config_clone);
        });
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**Benefits:**
- Config created once, shared everywhere
- No expensive clones of configuration data
- All workers see consistent config
- Automatic cleanup when all workers done


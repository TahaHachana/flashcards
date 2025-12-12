## Pattern Selection Example - Web Server

Walk through choosing the right smart pointer pattern for a web server request counter. What are the requirements and what pattern fits?

---

**Requirements:**
- Multiple threads handling requests
- Shared counter incremented on each request
- Simple read/write pattern
- Need accurate count

**Decision process:**
```
Need multiple owners?
└─ Yes (multiple request handler threads)
    └─ Single or multi-threaded?
        └─ Multi-threaded (concurrent requests)
            └─ Need mutability?
                └─ Yes (increment counter)
                    └─ Read-heavy or balanced?
                        └─ Balanced (increment is write)
                            └─ Pattern: Arc<Mutex<T>>
```

**Implementation:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

struct Server {
    request_count: Arc<Mutex<u64>>,
}

impl Server {
    fn handle_request(&self) {
        // Increment counter
        *self.request_count.lock().unwrap() += 1;
        
        // Handle request...
    }
    
    fn get_count(&self) -> u64 {
        *self.request_count.lock().unwrap()
    }
}

fn main() {
    let server = Arc::new(Server {
        request_count: Arc::new(Mutex::new(0)),
    });
    
    // Spawn request handlers
    for _ in 0..10 {
        let server_clone = Arc::clone(&server);
        thread::spawn(move || {
            server_clone.handle_request();
        });
    }
}
```

**Why this pattern:**
- `Arc`: Multiple threads share counter
- `Mutex`: Counter is modified (not read-heavy)
- Simple and correct


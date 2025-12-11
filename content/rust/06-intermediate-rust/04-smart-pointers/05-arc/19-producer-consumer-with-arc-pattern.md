## Producer-Consumer with Arc Pattern

Implement a producer-consumer pattern using `Arc<Mutex<Vec>>` for a shared queue.

---

```rust
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

fn main() {
    let queue = Arc::new(Mutex::new(Vec::new()));
    
    // Producer thread
    let queue_clone = Arc::clone(&queue);
    let producer = thread::spawn(move || {
        for i in 0..10 {
            queue_clone.lock().unwrap().push(i);
            println!("Produced: {}", i);
            thread::sleep(Duration::from_millis(100));
        }
    });
    
    // Consumer thread
    let queue_clone = Arc::clone(&queue);
    let consumer = thread::spawn(move || {
        loop {
            let item = {
                let mut queue = queue_clone.lock().unwrap();
                queue.pop()
            };  // Lock released
            
            if let Some(item) = item {
                println!("Consumed: {}", item);
                thread::sleep(Duration::from_millis(150));
            } else {
                thread::sleep(Duration::from_millis(50));
            }
        }
    });
    
    producer.join().unwrap();
    // Consumer runs forever in this example
}
```

**Pattern:**
- Shared queue wrapped in `Arc<Mutex<Vec>>`
- Producer adds items
- Consumer removes items
- Both can run concurrently
- Mutex ensures safe access


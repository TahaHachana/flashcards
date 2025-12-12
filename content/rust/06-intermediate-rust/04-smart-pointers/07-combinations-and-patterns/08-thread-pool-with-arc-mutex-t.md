## Thread Pool with Arc<Mutex<T>>

Demonstrate using `Arc<Mutex<T>>` to implement a shared work queue for a thread pool.

---

```rust
use std::sync::{Arc, Mutex};
use std::thread;
use std::collections::VecDeque;

type Job = Box<dyn FnOnce() + Send + 'static>;

struct WorkQueue {
    jobs: Arc<Mutex<VecDeque<Job>>>,
}

impl WorkQueue {
    fn new() -> Self {
        WorkQueue {
            jobs: Arc::new(Mutex::new(VecDeque::new())),
        }
    }
    
    fn push(&self, job: Job) {
        self.jobs.lock().unwrap().push_back(job);
    }
    
    fn pop(&self) -> Option<Job> {
        self.jobs.lock().unwrap().pop_front()
    }
    
    fn spawn_workers(&self, count: usize) {
        for id in 0..count {
            let jobs_clone = Arc::clone(&self.jobs);
            
            thread::spawn(move || {
                loop {
                    let job = jobs_clone.lock().unwrap().pop_front();
                    
                    match job {
                        Some(job) => job(),
                        None => thread::sleep(Duration::from_millis(10)),
                    }
                }
            });
        }
    }
}
```

**Why Arc<Mutex<T>>?**
- Multiple worker threads need access → `Arc`
- Queue is modified (push/pop) → `Mutex`
- Workers run concurrently → Thread-safe


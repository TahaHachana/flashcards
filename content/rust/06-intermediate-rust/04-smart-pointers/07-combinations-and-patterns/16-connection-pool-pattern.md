## Connection Pool Pattern

Implement a connection pool using `Arc<Mutex<T>>` that multiple threads can acquire and release connections from.

---

```rust
use std::sync::{Arc, Mutex};
use std::collections::VecDeque;
use std::thread;

struct Connection {
    id: usize,
}

struct ConnectionPool {
    connections: Arc<Mutex<VecDeque<Connection>>>,
}

impl ConnectionPool {
    fn new(size: usize) -> Self {
        let mut connections = VecDeque::new();
        for id in 0..size {
            connections.push_back(Connection { id });
        }
        
        ConnectionPool {
            connections: Arc::new(Mutex::new(connections)),
        }
    }
    
    fn acquire(&self) -> Option<Connection> {
        self.connections.lock().unwrap().pop_front()
    }
    
    fn release(&self, conn: Connection) {
        self.connections.lock().unwrap().push_back(conn);
    }
    
    fn available(&self) -> usize {
        self.connections.lock().unwrap().len()
    }
}

fn main() {
    let pool = Arc::new(ConnectionPool::new(5));
    let mut handles = vec![];
    
    for i in 0..10 {
        let pool_clone = Arc::clone(&pool);
        
        let handle = thread::spawn(move || {
            if let Some(conn) = pool_clone.acquire() {
                println!("Thread {} got connection {}", i, conn.id);
                thread::sleep(Duration::from_millis(100));
                pool_clone.release(conn);
            }
        });
        
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```

**Pattern:** Multiple threads safely share and modify a pool of resources.


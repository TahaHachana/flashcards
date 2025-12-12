## Deadlock Problem

What is a deadlock with `Arc<Mutex<T>>`, show an example, and explain why it happens.

---

**What is deadlock?**
When two or more threads wait for each other indefinitely, unable to proceed.

**Example:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let mutex1 = Arc::new(Mutex::new(0));
    let mutex2 = Arc::new(Mutex::new(0));
    
    // Thread 1: locks mutex1, then mutex2
    let m1 = Arc::clone(&mutex1);
    let m2 = Arc::clone(&mutex2);
    thread::spawn(move || {
        let _g1 = m1.lock().unwrap();
        println!("Thread 1: locked mutex1");
        thread::sleep(Duration::from_millis(10));
        
        let _g2 = m2.lock().unwrap();  // ⚠️ Waiting for Thread 2
        println!("Thread 1: locked mutex2");
    });
    
    // Thread 2: locks mutex2, then mutex1
    let m1 = Arc::clone(&mutex1);
    let m2 = Arc::clone(&mutex2);
    thread::spawn(move || {
        let _g2 = m2.lock().unwrap();
        println!("Thread 2: locked mutex2");
        thread::sleep(Duration::from_millis(10));
        
        let _g1 = m1.lock().unwrap();  // ⚠️ Waiting for Thread 1
        println!("Thread 2: locked mutex1");
    });
    
    thread::sleep(Duration::from_secs(1));
    // Program hangs - deadlock!
}
```

**Why it deadlocks:**
```
Time  Thread 1              Thread 2
────────────────────────────────────────
t0    Lock mutex1           Lock mutex2
t1    Wait for mutex2 ────→ Wait for mutex1
t2    ← Both stuck waiting forever →
```

Thread 1 holds mutex1 and waits for mutex2.
Thread 2 holds mutex2 and waits for mutex1.
Neither can proceed - deadlock!


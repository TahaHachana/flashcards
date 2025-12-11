## Gotcha - Deadlocks

What is a deadlock with `Arc<Mutex<T>>`, how does it happen, and how do you prevent it?

---

**A deadlock occurs when threads wait for each other indefinitely.**

**The problem:**
```rust
use std::sync::{Arc, Mutex};
use std::thread;

let data1 = Arc::new(Mutex::new(0));
let data2 = Arc::new(Mutex::new(0));

let d1 = Arc::clone(&data1);
let d2 = Arc::clone(&data2);

// Thread 1: locks data1, then data2
thread::spawn(move || {
    let _g1 = d1.lock().unwrap();
    thread::sleep(Duration::from_millis(10));
    let _g2 = d2.lock().unwrap();  // ⚠️ Waits for Thread 2
});

let d1 = Arc::clone(&data1);
let d2 = Arc::clone(&data2);

// Thread 2: locks data2, then data1
thread::spawn(move || {
    let _g2 = d2.lock().unwrap();
    thread::sleep(Duration::from_millis(10));
    let _g1 = d1.lock().unwrap();  // ⚠️ Waits for Thread 1
});
// Both threads wait forever - deadlock!
```

**Why it happens:**
- Thread 1 holds lock on data1, waits for data2
- Thread 2 holds lock on data2, waits for data1
- Neither can proceed

**Solution: Always lock in the same order**
```rust
// Both threads lock data1 first, then data2
thread::spawn(move || {
    let _g1 = d1.lock().unwrap();  // Always lock data1 first
    let _g2 = d2.lock().unwrap();
});

thread::spawn(move || {
    let _g1 = d1.lock().unwrap();  // Same order here
    let _g2 = d2.lock().unwrap();
});
```


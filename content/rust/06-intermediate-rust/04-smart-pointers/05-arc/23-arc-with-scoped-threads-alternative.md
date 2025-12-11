## Arc with Scoped Threads Alternative

When can you avoid using `Arc` by using scoped threads instead?

---

**Scoped threads** can borrow data without requiring `Arc`, as long as threads complete within a defined scope.

**Without scoped threads (needs Arc):**
```rust
use std::sync::Arc;
use std::thread;

let data = Arc::new(vec![1, 2, 3]);

let handle = thread::spawn(move || {
    // Needs Arc because thread might outlive data
    println!("{:?}", data);
});

handle.join().unwrap();
```

**With scoped threads (no Arc needed):**
```rust
use std::thread;

let data = vec![1, 2, 3];

thread::scope(|s| {
    s.spawn(|| {
        // Can borrow! Scope guarantees thread ends before data dies
        println!("{:?}", data);
    });
    
    s.spawn(|| {
        println!("{:?}", data);  // Multiple borrows OK
    });
    
    // All threads automatically joined at end of scope
});
```

**Why it works:**
- Scope guarantees threads complete before scope ends
- Data guaranteed to outlive threads
- No need for ownership transfer
- Follows normal borrowing rules

**When to use each:**
- **Scoped threads**: Threads complete within defined scope, can borrow
- **Regular threads + Arc**: Threads may outlive scope, need shared ownership

**Benefit:** Simpler code when scoped threads fit the use case.


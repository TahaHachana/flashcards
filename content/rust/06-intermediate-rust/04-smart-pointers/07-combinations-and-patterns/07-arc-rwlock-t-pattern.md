## Arc<RwLock<T>> Pattern

What is `Arc<RwLock<T>>`, when should you use it instead of `Arc<Mutex<T>>`, and what are the trade-offs?

---

**What it provides:**
```
Arc<RwLock<T>>
│
├─ Arc: Multiple threads can share the same data
│
└─ RwLock: Multiple readers OR one writer at a time
```

**Capabilities:**
- ✅ Multiple concurrent readers
- ✅ Exclusive writer access
- ✅ Better performance when reads >> writes
- ⚠️ More complex than Mutex

**Use Arc<RwLock<T>> when:**
- Reads are much more common than writes (10:1 or more)
- Read operations are slow enough that concurrency helps
- Multiple readers benefit from parallelism
- Writer starvation isn't a concern

**Use Arc<Mutex<T>> when:**
- Reads and writes balanced
- Simple locking logic needed
- Operations are fast
- Default choice

**Example:**
```rust
use std::sync::{Arc, RwLock};

let data = Arc::new(RwLock::new(vec![1, 2, 3]));

// Many readers (can read concurrently)
let read_guard = data.read().unwrap();
println!("{:?}", *read_guard);

// One writer (exclusive access)
let mut write_guard = data.write().unwrap();
write_guard.push(4);
```

**Performance:**
```
90% reads, 10% writes:
Mutex:  ~100ms for 1M operations
RwLock: ~60ms for 1M operations

50% reads, 50% writes:
Mutex:  ~100ms
RwLock: ~120ms (worse!)
```


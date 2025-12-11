## Rc and Garbage Collection Comparison

How is `Rc` similar to and different from garbage collection in languages like Java or Python?

---

**Similarities:**
- Automatic memory management
- No manual `free()` or `delete` needed
- Data cleaned up when no longer referenced
- Tracks how many references exist

**Key differences:**

| Aspect | Rc | Garbage Collection |
|--------|-----|-------------------|
| **When** | Deterministic (when count = 0) | Non-deterministic (GC runs eventually) |
| **Overhead** | Reference counting only | Runtime with GC pauses |
| **Cycles** | Leaks (need Weak) | Handled automatically |
| **Predictability** | Immediate cleanup | Unpredictable timing |
| **Performance** | No pauses | Can pause program |

**Example showing determinism:**
```rust
use std::rc::Rc;

struct Data(String);

impl Drop for Data {
    fn drop(&mut self) {
        println!("Dropped: {}", self.0);
    }
}

fn main() {
    let rc = Rc::new(Data("data".to_string()));
    {
        let rc2 = Rc::clone(&rc);
        println!("Using data");
    }  // rc2 dropped here, count: 1
    println!("Still using");
}  // rc dropped here, count: 0, IMMEDIATELY prints "Dropped: data"
```

**In GC languages:** Drop timing is unpredictable.
**With Rc:** Drop happens immediately when last Rc is dropped.

**Trade-off:** Rc requires handling cycles manually (Weak), but provides deterministic cleanup.


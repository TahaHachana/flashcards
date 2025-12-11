## When Rc Drops Data

Explain precisely when `Rc` drops the inner data. Show with an example tracking the lifecycle.

---

Data is dropped when the **strong count reaches zero**, regardless of weak count.

**Example tracking lifecycle:**
```rust
use std::rc::Rc;

struct Data {
    value: String,
}

impl Drop for Data {
    fn drop(&mut self) {
        println!("Dropping: {}", self.value);
    }
}

fn main() {
    println!("Creating rc1");
    let rc1 = Rc::new(Data {
        value: "data".to_string(),
    });
    println!("Count: {}", Rc::strong_count(&rc1));  // 1
    
    {
        println!("Creating rc2");
        let rc2 = Rc::clone(&rc1);
        println!("Count: {}", Rc::strong_count(&rc1));  // 2
        
        println!("Creating weak");
        let weak = Rc::downgrade(&rc1);
        println!("Strong: {}, Weak: {}",
                 Rc::strong_count(&rc1),
                 Rc::weak_count(&rc1));  // Strong: 2, Weak: 1
        
        println!("Dropping rc2");
    }  // rc2 dropped, count: 1
    
    println!("Count: {}", Rc::strong_count(&rc1));  // 1
    println!("Dropping rc1");
}  // rc1 dropped, count: 0, data is freed

// Output:
// Creating rc1
// Count: 1
// Creating rc2
// Count: 2
// Creating weak
// Strong: 2, Weak: 1
// Dropping rc2
// Count: 1
// Dropping rc1
// Dropping: data
```

**Rule:** Strong count = 0 → Drop, regardless of weak count.


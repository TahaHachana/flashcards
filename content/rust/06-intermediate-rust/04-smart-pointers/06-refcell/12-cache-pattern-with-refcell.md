## Cache Pattern with RefCell

Implement a cache using `RefCell` that computes values on first access and returns cached values on subsequent accesses.

---

```rust
use std::cell::RefCell;
use std::collections::HashMap;

struct Cache {
    data: RefCell<HashMap<String, String>>,
}

impl Cache {
    fn new() -> Self {
        Cache {
            data: RefCell::new(HashMap::new()),
        }
    }
    
    fn get(&self, key: &str) -> Option<String> {
        self.data.borrow().get(key).cloned()
    }
    
    fn set(&self, key: String, value: String) {
        self.data.borrow_mut().insert(key, value);
    }
    
    fn get_or_compute<F>(&self, key: &str, compute: F) -> String
    where
        F: FnOnce() -> String,
    {
        // Check cache first (short borrow)
        if let Some(value) = self.get(key) {
            return value;
        }
        
        // Compute (no borrow held)
        let value = compute();
        
        // Cache result
        self.set(key.to_string(), value.clone());
        value
    }
}

fn main() {
    let cache = Cache::new();
    
    let result1 = cache.get_or_compute("key1", || {
        println!("Computing...");
        "expensive_result".to_string()
    });  // Prints "Computing..."
    
    let result2 = cache.get_or_compute("key1", || {
        println!("Computing...");
        "expensive_result".to_string()
    });  // Doesn't print - cached!
}
```

**Pattern:** Lazy evaluation with memoization through immutable API.


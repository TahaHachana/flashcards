## Caching Pattern with Rc

Show how to use `Rc` for caching/memoization where expensive data is shared.

---

```rust
use std::rc::Rc;
use std::collections::HashMap;

struct ExpensiveData {
    content: String,
}

impl ExpensiveData {
    fn compute(key: &str) -> Self {
        // Simulate expensive computation
        ExpensiveData {
            content: format!("Computed data for {}", key),
        }
    }
}

struct Cache {
    data: HashMap<String, Rc<ExpensiveData>>,
}

impl Cache {
    fn new() -> Self {
        Cache { data: HashMap::new() }
    }
    
    fn get(&mut self, key: &str) -> Rc<ExpensiveData> {
        self.data
            .entry(key.to_string())
            .or_insert_with(|| {
                Rc::new(ExpensiveData::compute(key))
            })
            .clone()  // Cheap Rc clone, not data clone!
    }
}

fn main() {
    let mut cache = Cache::new();
    
    let data1 = cache.get("key1");
    let data2 = cache.get("key1");  // Same Rc, not recomputed
    
    // Both point to same data
    assert!(Rc::ptr_eq(&data1, &data2));
}
```

**Benefits:**
- Expensive data computed only once
- Multiple users can hold references
- Data stays in cache as long as anyone uses it
- Automatic cleanup when all users done


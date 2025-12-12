## Pattern Selection Example - Config Service

Walk through choosing the right smart pointer pattern for a configuration service. What are the requirements and what pattern fits?

---

**Requirements:**
- Multiple threads reading config
- Rare config updates (mostly reads)
- Config reads are frequent
- Updates need to be visible to all threads

**Decision process:**
```
Need multiple owners?
└─ Yes (multiple threads access config)
    └─ Single or multi-threaded?
        └─ Multi-threaded (concurrent access)
            └─ Need mutability?
                └─ Yes (rare updates)
                    └─ Read-heavy or balanced?
                        └─ Read-heavy (90%+ reads)
                            └─ Pattern: Arc<RwLock<T>>
```

**Implementation:**
```rust
use std::sync::{Arc, RwLock};
use std::collections::HashMap;

type Config = Arc<RwLock<HashMap<String, String>>>;

struct ConfigService {
    config: Config,
}

impl ConfigService {
    fn new() -> Self {
        ConfigService {
            config: Arc::new(RwLock::new(HashMap::new())),
        }
    }
    
    fn get(&self, key: &str) -> Option<String> {
        self.config.read().unwrap().get(key).cloned()
    }
    
    fn set(&self, key: String, value: String) {
        self.config.write().unwrap().insert(key, value);
    }
}
```

**Why this pattern:**
- `Arc`: Multiple threads share config
- `RwLock`: Many concurrent reads, rare writes
- Better performance than `Mutex` for this access pattern

**Alternative:** Could use `Arc<Mutex<T>>` if simplicity preferred over read performance.


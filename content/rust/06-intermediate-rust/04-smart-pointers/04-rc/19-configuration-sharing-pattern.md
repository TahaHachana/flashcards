## Configuration Sharing Pattern

Demonstrate using `Rc` to share configuration across multiple components without cloning.

---

```rust
use std::rc::Rc;

struct Config {
    database_url: String,
    max_connections: u32,
    timeout_ms: u64,
}

struct App {
    config: Rc<Config>,
}

struct DatabasePool {
    config: Rc<Config>,
}

struct Logger {
    config: Rc<Config>,
}

fn main() {
    // Create config once
    let config = Rc::new(Config {
        database_url: "postgres://localhost".to_string(),
        max_connections: 100,
        timeout_ms: 5000,
    });
    
    // Share across components (cheap)
    let app = App {
        config: Rc::clone(&config),
    };
    
    let pool = DatabasePool {
        config: Rc::clone(&config),
    };
    
    let logger = Logger {
        config: Rc::clone(&config),
    };
    
    // All share the same config
    println!("Connections: {}", app.config.max_connections);
    println!("Strong count: {}", Rc::strong_count(&config));  // 4
}
```

**Benefits:**
- Config created once, shared everywhere
- No expensive clones of configuration data
- All components see consistent config
- Automatic cleanup when last component drops


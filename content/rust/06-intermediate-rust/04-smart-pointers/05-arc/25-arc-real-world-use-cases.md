## Arc Real-World Use Cases

Provide four real-world scenarios where `Arc` is the right choice.

---

**1. Web server with shared connection pool:**
```rust
use std::sync::Arc;

struct ConnectionPool {
    connections: Vec<Connection>,
}

let pool = Arc::new(ConnectionPool::new());

// Each request handler gets a clone
for _ in 0..100 {
    let pool_clone = Arc::clone(&pool);
    thread::spawn(move || {
        handle_request(pool_clone);
    });
}
```

**2. Game engine with shared world state:**
```rust
struct GameWorld {
    entities: HashMap<EntityId, Entity>,
    physics: PhysicsEngine,
}

let world = Arc::new(RwLock::new(GameWorld::new()));

// Rendering thread (read)
let world_clone = Arc::clone(&world);
thread::spawn(move || {
    render_loop(world_clone);
});

// Physics thread (write)
let world_clone = Arc::clone(&world);
thread::spawn(move || {
    physics_loop(world_clone);
});
```

**3. Multi-threaded logger:**
```rust
struct Logger {
    logs: Mutex<Vec<LogEntry>>,
    config: LogConfig,
}

static LOGGER: Arc<Logger> = ...;

// Any thread can log
thread::spawn(move || {
    LOGGER.log("Event happened");
});
```

**4. Parallel data processing with shared results:**
```rust
let results = Arc::new(Mutex::new(Vec::new()));

for chunk in data.chunks(1000) {
    let results_clone = Arc::clone(&results);
    thread::spawn(move || {
        let processed = process_chunk(chunk);
        results_clone.lock().unwrap().push(processed);
    });
}
```

**Common thread:** Arc enables safe sharing of data across multiple threads in concurrent systems.


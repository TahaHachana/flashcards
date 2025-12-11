## Logger Pattern with RefCell

Implement a logger using `RefCell` that can accumulate log messages through immutable references.

---

```rust
use std::cell::RefCell;

struct Logger {
    logs: RefCell<Vec<String>>,
}

impl Logger {
    fn new() -> Self {
        Logger {
            logs: RefCell::new(Vec::new()),
        }
    }
    
    // Takes &self, not &mut self
    fn log(&self, message: &str) {
        self.logs.borrow_mut().push(message.to_string());
    }
    
    fn get_logs(&self) -> Vec<String> {
        self.logs.borrow().clone()
    }
}

fn main() {
    let logger = Logger::new();
    
    // Can pass &Logger to functions
    process_data(&logger);
    process_more_data(&logger);
    
    println!("Logs: {:?}", logger.get_logs());
}

fn process_data(logger: &Logger) {
    logger.log("Processing data");
}

fn process_more_data(logger: &Logger) {
    logger.log("Processing more data");
}
```

**Why RefCell?**
- Functions take `&Logger`, not `&mut Logger`
- Still need to mutate internal state (add logs)
- RefCell provides interior mutability
- Single-threaded context (use Mutex for multi-threaded)


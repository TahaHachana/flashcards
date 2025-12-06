## Factory Pattern with Box

Demonstrate the factory pattern using `Box<dyn Trait>` to return different types based on runtime conditions.

---

```rust
trait Logger {
    fn log(&self, message: &str);
}

struct FileLogger;
impl Logger for FileLogger {
    fn log(&self, message: &str) {
        println!("File: {}", message);
    }
}

struct ConsoleLogger;
impl Logger for ConsoleLogger {
    fn log(&self, message: &str) {
        println!("Console: {}", message);
    }
}

// Factory function
fn create_logger(use_file: bool) -> Box<dyn Logger> {
    if use_file {
        Box::new(FileLogger)
    } else {
        Box::new(ConsoleLogger)
    }
}

fn main() {
    let logger = create_logger(true);
    logger.log("Hello");  // File: Hello
    
    let logger = create_logger(false);
    logger.log("World");  // Console: World
}
```

**Pattern benefits:**
- Encapsulates object creation logic
- Returns different types through same interface
- Caller doesn't need to know concrete type


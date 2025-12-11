## When to Use RefCell

List four good use cases and three bad use cases for `RefCell`.

---

**✅ Good use cases:**

**1. API requires immutable reference:**
```rust
trait Logger {
    fn log(&self, msg: &str);  // Must take &self
}

struct FileLogger {
    logs: RefCell<Vec<String>>,  // Can mutate!
}
```

**2. Mock objects in tests:**
```rust
struct MockDatabase {
    calls: RefCell<Vec<String>>,  // Track method calls
}
```

**3. Caching/memoization:**
```rust
struct Calculator {
    cache: RefCell<HashMap<String, i32>>,
}
```

**4. Graph/tree with parent pointers:**
```rust
struct Node {
    children: RefCell<Vec<Rc<Node>>>,
}
```

**❌ Bad use cases:**

**1. Regular mut works:**
```rust
// Just use let mut instead
```

**2. Multi-threaded context:**
```rust
// Use Mutex instead - RefCell is not thread-safe
```

**3. Can restructure to avoid:**
```rust
// Prefer compile-time safety when possible
```

**Rule:** Use RefCell only when architecture demands mutability through immutable references.


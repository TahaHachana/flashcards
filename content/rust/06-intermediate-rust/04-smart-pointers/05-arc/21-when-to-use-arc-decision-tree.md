## When to Use Arc Decision Tree

Create a decision tree for when to use `Arc`, `Rc`, or neither.

---

```
Need shared ownership?
  │
  ├─ No → Use regular ownership or Box
  │       Don't add unnecessary complexity
  │
  └─ Yes → Multiple threads?
      │
      ├─ No (single-threaded)
      │   │
      │   └─ Use Rc<T>
      │       ├─ Need mutation? → Rc<RefCell<T>>
      │       └─ Read-only? → Rc<T>
      │
      └─ Yes (multi-threaded)
          │
          └─ Use Arc<T>
              ├─ Need mutation? → Arc<Mutex<T>> or Arc<RwLock<T>>
              │   ├─ Many readers, few writers? → Arc<RwLock<T>>
              │   └─ General case? → Arc<Mutex<T>>
              └─ Read-only? → Arc<T>
```

**Examples:**
```rust
// Single owner
let data = String::from("hello");

// Multiple owners, one thread
let data = Rc::new(String::from("hello"));

// Multiple owners, multiple threads
let data = Arc::new(String::from("hello"));

// Shared mutable, multiple threads
let data = Arc::new(Mutex::new(vec![]));
```

**Rule of thumb:** Start simple (regular ownership), add complexity only when needed.


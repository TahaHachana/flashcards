## Arc<Mutex<T>> vs Rc<RefCell<T>>

Compare `Rc<RefCell<T>>` and `Arc<Mutex<T>>`. When do you use each?

---

```markdown
| Feature           | Rc<RefCell<T>>   | Arc<Mutex<T>>     |
|-------------------|------------------|-------------------|
| Thread-safe       | No               | Yes               |
| Overhead          | Small            | Larger            |
| Borrow checking   | Runtime          | Runtime (via lock)|
| Performance       | ~5ns per borrow  | ~100ns per lock   |
| Use case          | Single-threaded  | Multi-threaded    |
```

**Use Rc<RefCell<T>> when:**
- ✅ Guaranteed single-threaded
- ✅ Need best performance
- ✅ Building UI or game engine
- ✅ Complex data structures

**Use Arc<Mutex<T>> when:**
- ✅ Might use threads now or later
- ✅ Need thread safety
- ✅ Building server or concurrent system
- ✅ Shared state across threads

**Performance comparison:**
```rust
// Single-threaded: Rc<RefCell<T>>
let data = Rc::new(RefCell::new(vec![]));
data.borrow_mut().push(1);  // ~5ns overhead

// Multi-threaded: Arc<Mutex<T>>
let data = Arc::new(Mutex::new(vec![]));
data.lock().unwrap().push(1);  // ~100ns overhead
```

**Rule:** Choose based on threading requirements, not micro-optimizations.


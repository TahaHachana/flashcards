## RefCell vs Mutex Pattern

When should you use RefCell<T> vs Mutex<T> for interior mutability?

---

Use RefCell<T> for single-threaded interior mutability - it has no synchronization overhead but isn't Sync. Use Mutex<T> for multi-threaded interior mutability - it provides thread-safe access but has locking overhead. The rule: if your code involves threads, use Mutex. If it's strictly single-threaded and you need interior mutability, RefCell is more efficient. Don't use RefCell just because you want to avoid thinking about locking.


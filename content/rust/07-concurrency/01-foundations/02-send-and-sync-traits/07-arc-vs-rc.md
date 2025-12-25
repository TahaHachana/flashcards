## Arc vs Rc

What is the difference between Rc<T> and Arc<T>, and when should you use each?

---

Rc<T> uses non-atomic reference counting and is not Send/Sync - use it for single-threaded shared ownership. Arc<T> uses atomic reference counting and is Send/Sync - use it for multi-threaded shared ownership. Arc has atomic operation overhead, so only use it when you actually need thread safety. The rule: single-threaded = Rc, multi-threaded = Arc.


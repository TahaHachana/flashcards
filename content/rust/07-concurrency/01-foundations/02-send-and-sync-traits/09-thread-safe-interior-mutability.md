## Thread-Safe Interior Mutability

What types provide thread-safe interior mutability, and why are they Sync when Cell/RefCell are not?

---

Mutex<T> and RwLock<T> provide thread-safe interior mutability. They are Sync (when T is Send) because they use locking to ensure only one thread can access the data at a time, preventing data races. Cell/RefCell have no synchronization and assume single-threaded access, so they're not Sync. The synchronization overhead is the cost of thread safety.


## Interior Mutability Thread Safety

What's the difference between RefCell and Mutex for interior mutability, and why can't you use RefCell with Arc?

---

RefCell provides single-threaded interior mutability with runtime borrow checking but no synchronization - it's not Sync. Mutex provides thread-safe interior mutability with locking - it is Sync. Arc<RefCell<T>> won't compile because RefCell isn't Sync, meaning you can't share it between threads. You must use Arc<Mutex<T>> for shared mutable state across threads. The type system enforces this distinction at compile time.


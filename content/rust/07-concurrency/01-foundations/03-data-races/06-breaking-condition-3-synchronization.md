## Breaking Condition 3 Synchronization

How does Rust enforce the third condition (synchronization) to prevent data races?

---

Rust provides synchronization primitives like Mutex<T> and RwLock<T> that enforce synchronized access through the type system. You can't access the data inside a Mutex without first acquiring the lock, which the type system enforces. Only one thread can hold the lock at a time, guaranteeing synchronized access. The type system makes synchronization mandatory, not optional.


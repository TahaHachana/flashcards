## Connection to Smart Pointers

How do concurrency primitives relate to the smart pointers you've learned?

---

Concurrency primitives are smart pointers that extend ownership to concurrent contexts. `Arc<T>` (Atomic Reference Counted) allows shared ownership across threads, similar to `Rc<T>` but thread-safe. `Mutex<T>` provides interior mutability for shared data, similar to `RefCell<T>` but with thread-safe locking. These types compose (like `Arc<Mutex<T>>`) to provide both shared ownership and synchronized mutation across threads.


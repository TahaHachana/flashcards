## Preventing Concurrent Mutation

Why can't you capture a mutable reference in a closure passed to thread::spawn?

---

The closure might outlive the current scope (threads can run indefinitely), and Rust can't guarantee the mutable reference remains valid. Also, if both the parent thread and spawned thread had mutable access, they could mutate without synchronization, causing data races. The borrowing rules prevent this by not allowing mutable references to be captured in closures that outlive their scope. You must use move to transfer ownership or use Arc<Mutex<T>> for shared mutation.


## Send Without Sync Examples

Give examples of types that are Send but not Sync, and explain why.

---

Cell<T> and RefCell<T> are Send but not Sync. They're Send because you can transfer ownership to another thread (the new thread becomes the sole owner). They're not Sync because multiple threads can't safely share references to them - they have unsynchronized interior mutability. Also, mpsc::Sender and Receiver are Send but not Sync because they're designed for transfer between threads, not simultaneous access.


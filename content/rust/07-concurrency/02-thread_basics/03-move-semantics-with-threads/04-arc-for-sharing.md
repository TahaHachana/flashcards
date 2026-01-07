## Arc for Sharing

Why do you need Arc when multiple threads need access to the same data?

---

You can only move data once - after moving into one thread, it's no longer available to move into another. Arc (Atomic Reference Counted) allows shared ownership: Arc::clone creates new pointers to the same data, each can be moved into different threads. All Arc pointers share access to the same underlying data. Arc uses atomic operations for thread-safe reference counting, enabling safe sharing across threads.


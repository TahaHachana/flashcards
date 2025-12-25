## Static Variables and Sync

Why do static variables require their types to be Sync?

---

Static variables have 'static lifetime and can be accessed from any thread in the program. Multiple threads can have references to the same static variable simultaneously, so the type must be Sync to ensure this is safe. Without the Sync requirement, you could create data races by having multiple threads access a non-thread-safe static variable.


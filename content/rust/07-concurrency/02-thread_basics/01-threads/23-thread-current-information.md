## Thread Current Information

How can a thread get information about itself at runtime?

---

Use thread::current() which returns a handle to the currently executing thread. From this you can call: id() for a unique thread ID, and name() for the thread name (if set via Builder). Useful for logging, debugging, and identifying which thread is running code. Example: let name = thread::current().name(); println!("Running in thread: {:?}", name);


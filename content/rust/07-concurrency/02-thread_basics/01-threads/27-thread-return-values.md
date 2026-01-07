## Thread Return Values

How do threads return values, and how do you retrieve them?

---

The closure passed to spawn can return a value (the last expression). This value's type becomes T in JoinHandle<T>. Retrieve it by calling join() which returns Result<T, _>. Example: let h = thread::spawn(|| 42); let result = h.join().unwrap(); // result is 42. The value is moved out of the thread when join succeeds. If the thread panics, join returns Err instead of the value.


## Breaking Condition 1 Ownership

How does Rust's ownership system break the first condition of data races (multiple threads accessing same memory)?

---

Ownership ensures only one thread owns data at a time. When you move data into a thread with `move`, ownership is transferred - the original thread can no longer access it. This breaks the "multiple threads accessing same memory" condition because only the thread that owns the data can access it. No shared access means no data race is possible.


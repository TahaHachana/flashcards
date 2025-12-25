## Ownership Extension to Threads

How do Send and Sync extend Rust's ownership system to concurrent contexts?

---

Send and Sync apply ownership rules across thread boundaries. Send means "can transfer ownership between threads" (moving values), Sync means "can share references between threads" (borrowing). They leverage the same ownership, borrowing, and lifetime rules you already know, but enforce them across threads. The compiler uses these traits to ensure the ownership system's safety guarantees hold even in concurrent code, preventing data races at compile time.


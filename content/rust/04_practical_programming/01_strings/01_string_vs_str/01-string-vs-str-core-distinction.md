## String vs &str - Core Distinction

What are the two primary string types in Rust and what is the fundamental difference between them?

---

String and &str. String is an owned, heap-allocated, growable string type that you control and can modify. &str is a borrowed reference to UTF-8 data - an immutable view into existing string data that someone else owns. The distinction follows Rust's ownership philosophy: separating owned data from borrowed references.


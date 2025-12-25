## Type System Role

How does Rust's type system track and enforce thread safety to prevent data races?

---

The type system uses Send and Sync marker traits to track thread safety. The compiler automatically checks these traits when code uses types across threads. Types with unsynchronized interior mutability (like RefCell) are not Sync, so they can't be shared between threads. Types with non-atomic operations (like Rc) are not Send, so they can't be moved between threads. These compile-time checks prevent data races before the program runs.


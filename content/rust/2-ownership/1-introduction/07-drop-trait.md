## Drop Trait

How is cleanup handled when an owned value goes out of scope in Rust?

---

Rust automatically calls the `Drop` trait implementation for the value, freeing resources safely when the owner goes out of scope.


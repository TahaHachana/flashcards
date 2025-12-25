## Compile Time Verification

How do Send and Sync enable compile-time prevention of data races?

---

The compiler automatically checks Send/Sync when you use types across threads. If you try to send a non-Send type to another thread or share a non-Sync type between threads, compilation fails with a clear error. This means data races from violating thread safety are caught before the program even runs. The type system encodes thread safety as a compile-time property, not a runtime check.


## Type System Encodes Safety

How does the type system encode thread safety as a compile-time property?

---

Send and Sync are traits automatically derived based on type composition. The compiler checks these traits when code crosses thread boundaries, turning potential runtime data races into compile-time errors. Thread safety becomes a property you can reason about and enforce through generic bounds (T: Send + Sync). The type system makes thread safety explicit and verifiable, allowing the compiler to guarantee no data races without any runtime overhead.


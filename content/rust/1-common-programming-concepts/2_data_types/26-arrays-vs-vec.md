## Arrays vs Vec

When should you use an array versus a `Vec<T>` in Rust?

---

* **Array `[T; N]`**: fixed size known at compile time, stack-allocated, very fast.
* **Vec<T>**: dynamic size, heap-allocated, can grow/shrink at runtime.


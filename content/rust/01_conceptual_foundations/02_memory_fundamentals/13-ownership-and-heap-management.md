## Ownership and Heap Management

Why does Rust's ownership system primarily focus on heap memory?

---

Stack data is simple (fixed size, automatic cleanup, copied easily). Heap data is complex (dynamic size, must be freed, copying is expensive). Ownership ensures heap memory is freed safely without manual management or garbage collection.


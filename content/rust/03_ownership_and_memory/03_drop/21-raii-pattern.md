## RAII Pattern

What is the RAII pattern in Rust?

---

Resource Acquisition Is Initialization. Acquire resources in constructors, release in Drop. Ensures cleanup happens automatically when value goes out of scope.

```rust
// Lock acquired when guard created
let guard = mutex.lock();
// Lock automatically released when guard dropped
```


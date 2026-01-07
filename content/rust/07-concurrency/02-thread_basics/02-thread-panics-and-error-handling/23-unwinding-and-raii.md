## Unwinding and RAII

How does unwinding relate to RAII (Resource Acquisition Is Initialization)?

---

Unwinding ensures Drop is called even during panics, maintaining RAII guarantees. Resources (files, locks, memory) are automatically cleaned up when their owners go out of scope, whether normally or via panic. This is critical for correctness: locks are released, files are closed, memory is freed. RAII + unwinding = automatic cleanup even in failure cases. This is why Rust can guarantee resource safety across panics.


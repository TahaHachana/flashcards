## Resource Cleanup Guarantee

What cleanup guarantees does Rust provide during thread panics?

---

During unwinding, all local variables' Drop implementations are called in reverse order of creation. This guarantees: MutexGuard releases locks, File closes handles, Box/Vec/String free memory, custom Resources run cleanup code. The guarantee holds for all panics (unless using abort mode or panicking in Drop). This is why Rust can have safe concurrency - resources are always cleaned up even when threads fail.


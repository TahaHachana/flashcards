## Manual Implementation Dangers

When should you manually implement Send or Sync using unsafe impl, and what are the dangers?

---

Manually implement Send/Sync only when working with unsafe code where the compiler can't verify safety but you can guarantee it (like custom smart pointers or FFI wrappers). Dangers: incorrect implementation breaks Rust's safety guarantees and can cause data races, use-after-free, or undefined behavior. The auto-implementation is almost always correct - manual implementation requires deep understanding and careful safety proofs.


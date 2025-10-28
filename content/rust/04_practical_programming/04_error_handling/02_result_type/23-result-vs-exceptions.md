## Result Vs Exceptions

How does Rust's `Result` approach differ from exception-based error handling?

---

**Result (Rust):**
- Errors are explicit in function signatures
- Compiler enforces handling
- Errors are values, not control flow
- Zero-cost when not used (no runtime overhead)

**Exceptions (Java/Python):**
- Errors invisible in signatures
- Easy to forget to catch
- Control flow mechanism
- Runtime overhead for stack unwinding

Result makes errors visible and forces handling at compile time, preventing forgotten error cases.


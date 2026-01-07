## FFI Panic Boundary

Why must you catch panics before they cross FFI boundaries, and how?

---

Panics crossing into C code cause undefined behavior - C doesn't understand Rust's unwinding. Use catch_unwind in extern "C" functions to catch panics and convert them to error codes or return values. Pattern: extern "C" fn safe_call() -> i32 { match catch_unwind(|| risky()) { Ok(v) => v, Err(_) => -1 /* error code */ }}. This maintains the C calling convention's expectations.


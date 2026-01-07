## Connection to Error Handling

How do thread panics connect to Rust's overall error handling philosophy?

---

Thread panics are converted to Result by join(), integrating with Rust's error handling. Panics represent "thread failed" - an error the caller must handle. Use Result for expected errors, panic for bugs/invariant violations. In threads, panics are isolated errors that propagate via Result, not program termination. This unifies panic (unrecoverable within scope) with Result (recoverable at caller) - panics become errors at thread boundaries.


## Catch Unwind Purpose

What is std::panic::catch_unwind and when should you use it?

---

catch_unwind catches panics within a thread, preventing them from propagating. It returns Result: Ok(value) if the closure succeeds, Err(payload) if it panics. Use cases: (1) Plugin systems - isolate plugin failures, (2) FFI boundaries - prevent panics from crossing to C, (3) Retry logic - catch, log, retry, (4) Testing frameworks - isolate test failures. It allows recovery from panics without the thread terminating.


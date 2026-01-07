## Panic in Drop Gotcha

What happens if you panic inside a Drop implementation during unwinding, and what should you do instead?

---

Panicking in Drop while already unwinding (from another panic) causes immediate abort - the process terminates without further cleanup. This is because Rust can't handle multiple panics simultaneously. Never panic in Drop. Instead: log errors, return early, use Result for fallible cleanup. If cleanup must succeed, document it clearly and make it the caller's responsibility to not panic before dropping.


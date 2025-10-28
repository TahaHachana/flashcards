## What Are Unwrap And Expect?

What are `unwrap()` and `expect()` in Rust, and how do they differ from proper error handling?

---

`unwrap()` and `expect()` are methods on `Result<T, E>` and `Option<T>` that extract the success value but **panic** (crash) if there's an error or `None`.

They are **not** error handling - they're the opposite. They convert errors into panics (unrecoverable crashes). They're "escape hatches" from Rust's safe error handling, meant for:
- Prototyping
- Tests
- Proven invariants
- Examples

Use them sparingly in production code.


## What Is Result<T, E>?

What is `Result<T, E>` in Rust and how does it differ from `Option<T>`?

---

`Result<T, E>` is an enum that represents operations that can succeed or fail. It has two variants: `Ok(T)` (success with value) and `Err(E)` (failure with error).

Unlike `Option<T>` which only indicates presence/absence, `Result<T, E>` provides context about *why* something failed through the error type `E`. This makes errors explicit in the type signature and impossible to ignore.


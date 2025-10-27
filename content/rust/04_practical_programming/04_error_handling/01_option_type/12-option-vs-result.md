## Option Vs Result

How does `Option<T>` differ from `Result<T, E>` and when should you use each?

---

`Option<T>`:
- Represents presence or absence
- `Some(T)` or `None`
- No information about *why* there's no value

`Result<T, E>`:
- Represents success or failure
- `Ok(T)` or `Err(E)`
- Includes error information explaining what went wrong

Use `Option` when absence is expected and normal (e.g., finding an item in a collection). Use `Result` when you need to communicate why an operation failed.


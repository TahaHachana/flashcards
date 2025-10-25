## Remove Method Return

What does `.remove(&key)` return and why is this design useful?

---

Returns `Option<V>`:
- `Some(value)` if key existed and was removed
- `None` if key didn't exist

This allows you to get the removed value and handle the "key not found" case gracefully without panicking.


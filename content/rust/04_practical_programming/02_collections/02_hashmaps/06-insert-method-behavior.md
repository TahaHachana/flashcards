## Insert Method Behavior

What does `.insert(key, value)` return, and what happens if the key already exists?

---

Returns `Option<V>`:
- `None` if key didn't exist (new entry created)
- `Some(old_value)` if key existed (value overwritten)

If key exists, the old value is replaced and returned.


## Or Insert Method

What does `.or_insert(default)` do, and what type does it return?

---

Returns `&mut V` (mutable reference to the value):
- If key exists: returns mutable reference to existing value
- If key doesn't exist: inserts default value, returns mutable reference to it

Always returns a mutable reference, allowing in-place modification.


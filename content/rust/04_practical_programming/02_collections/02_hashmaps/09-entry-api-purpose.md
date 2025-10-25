## Entry API Purpose

What does the `.entry(key)` method return and why is it useful?

---

Returns an `Entry<K, V>` enum with two variants:
- `Occupied(OccupiedEntry)` if key exists
- `Vacant(VacantEntry)` if key doesn't exist

Useful because it provides efficient ways to insert/modify values based on key existence without multiple lookups.


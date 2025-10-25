## Entry Dereferencing Requirement

Why do you need the `*` in `*counts.entry(key).or_insert(0) += 1`?

---

Because `.or_insert()` returns `&mut V` (a mutable reference), not `V`. To modify the actual value, you must dereference it with `*` before incrementing. Without `*`, you'd try to increment a reference, which doesn't work.


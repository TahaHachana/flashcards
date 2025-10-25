## Safe Indexing with get()

Compare `vec[5]` vs `vec.get(5)`. When should you use each?

---

`vec[5]` panics if index out of bounds; returns direct value.
`vec.get(5)` returns `Option<&T>`: `Some(&value)` or `None`; never panics.
Use `vec[i]` when you're certain index exists; use `.get()` when index might be invalid.


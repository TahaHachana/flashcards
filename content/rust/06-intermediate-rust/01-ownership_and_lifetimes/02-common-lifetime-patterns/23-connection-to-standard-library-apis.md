## Connection to Standard Library APIs

Which standard library APIs use which common lifetime patterns?

---

- Pattern 1: `Vec::first`, `HashMap::get` (return reference from collection)
- Pattern 2: `cmp::max`, `slice::iter().max()` (return one of multiple inputs)
- Pattern 3: All getter methods on structs
- Pattern 8: All iterator adaptors (`map`, `filter`, etc.)
- Pattern 9: `str::split_at`, `slice::split_first` (return multiple references)
Understanding patterns helps you read and use these APIs intuitively.


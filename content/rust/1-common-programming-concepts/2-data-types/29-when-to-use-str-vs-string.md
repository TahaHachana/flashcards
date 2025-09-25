## When to Use \&str vs String

When should you use `&str` vs `String`?

---

* **&str**: read-only, borrowed string slices; function parameters when you don’t need ownership.
* **String**: owned, growable string; when you need to store or modify text.


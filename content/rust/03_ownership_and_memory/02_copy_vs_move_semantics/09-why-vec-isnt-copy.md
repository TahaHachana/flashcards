## Why Vec Isn't Copy

Why doesn't Vec<T> implement Copy?

---

Vec manages heap-allocated buffer. Same double-free issue as String - if both owned the same buffer, both would try to free it when going out of scope.


## Why String Isn't Copy

Why doesn't String implement Copy?

---

String owns heap-allocated data. If copied, both would point to the same heap. When going out of scope, both would try to free it (double-free bug). Move semantics prevent this.


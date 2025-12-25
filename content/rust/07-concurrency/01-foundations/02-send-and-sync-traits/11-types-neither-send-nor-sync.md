## Types Neither Send Nor Sync

What types are neither Send nor Sync, and why?

---

Rc<T> is neither Send nor Sync because it uses non-atomic reference counting that isn't thread-safe. Raw pointers (*const T and *mut T) are neither Send nor Sync by default because the compiler can't verify the pointed-to data will remain valid across thread boundaries. Any type containing these types also becomes neither Send nor Sync through composition.


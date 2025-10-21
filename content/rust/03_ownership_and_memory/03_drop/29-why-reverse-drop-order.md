## Why Reverse Drop Order

Why are values dropped in reverse order of creation?

---

Later values might depend on earlier ones. Dropping in reverse (LIFO) ensures dependencies are still valid when each value is dropped.


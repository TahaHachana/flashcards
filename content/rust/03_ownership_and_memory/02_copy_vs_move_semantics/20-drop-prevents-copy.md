## Drop Prevents Copy

Can a type implement both Copy and Drop?

---

No. A type with Drop cannot be Copy. Drop implies special cleanup, which doesn't make sense for a simple bit-wise copy.


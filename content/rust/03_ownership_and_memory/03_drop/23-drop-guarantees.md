## Drop Guarantees

What guarantees does Drop provide?

---

Exactly once (each value dropped once unless moved/forgotten), reverse order (LIFO), runs on panic (during unwinding), automatic (compiler inserts), and scope-based (runs when owner goes out of scope).


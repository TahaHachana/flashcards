## Copy Requires Clone

Why must you derive both Copy and Clone?

---

Copy is a subtrait of Clone. All Copy types must also implement Clone, so you must derive both.


## Big Omega Notation

What does Ω (Big Omega) notation represent, and how does it differ from Big O?

---

**Ω(g(n))** represents a **lower bound**: f(n) = Ω(g(n)) if |f(n)| ≥ C|g(n)| for all n ≥ n₀.

**Difference from O**:
- **O (Big O)**: Upper bound - function grows no faster than g(n)
- **Ω (Omega)**: Lower bound - function grows no slower than g(n)

Example: 16n³ + 24n = Ω(n³) means the function grows at least as fast as n³.


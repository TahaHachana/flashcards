## Big Theta Notation

What is the significance of Θ (Big Theta) notation, and what must be true for f(n) = Θ(g(n))?

---

**Θ (Theta)** represents a **tight bound** - both upper and lower bound simultaneously.

f(n) = Θ(g(n)) means:
- C₁|g(n)| ≤ |f(n)| ≤ C₂|g(n)| for all n ≥ n₀
- Equivalently: f(n) = O(g(n)) AND f(n) = Ω(g(n))

**Significance**: The growth rate of f(n) is exactly g(n) (within constant factors). Example: 28n + 9 = Θ(n) because it's bounded both above and below by linear functions.


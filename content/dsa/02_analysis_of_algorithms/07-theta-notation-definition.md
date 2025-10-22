## Theta Notation Definition

Define Theta notation Θ(g(n)) and explain what it represents.

---

f(n) = Θ(g(n)) if there exist positive constants c₁, c₂, and n₀ such that c₁|g(n)| ≤ |f(n)| ≤ c₂|g(n)| for all n ≥ n₀.

Theta represents a tight bound - g(n) is both an upper and lower bound for f(n). Equivalently, f(n) = Θ(g(n)) if and only if f(n) = O(g(n)) AND f(n) = Ω(g(n)). It means f(n) grows at exactly the same rate as g(n).


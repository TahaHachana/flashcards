## Big O Notation Definition

Define Big O notation mathematically and explain what it means for f(n) = O(g(n)).

---

**Definition**: f(n) = O(g(n)) if there exists a positive integer n₀ and positive constant C such that |f(n)| ≤ C|g(n)| for all n ≥ n₀.

**Meaning**: g(n) serves as an **upper bound** for f(n). The function f(n) grows no faster than g(n) (times some constant) for sufficiently large n. This is the most commonly used notation in algorithm analysis.


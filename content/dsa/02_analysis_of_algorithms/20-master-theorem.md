## Master Theorem Overview

For recurrences of the form T(n) = aT(n/b) + f(n), what are the three cases of the Master Theorem and their outcomes?

---

**Case 1**: If f(n) = O(n^(log_b(a) - ε)) for ε > 0
→ T(n) = Θ(n^(log_b a))

**Case 2**: If f(n) = Θ(n^(log_b a))
→ T(n) = Θ(n^(log_b a) log n)

**Case 3**: If f(n) = Ω(n^(log_b(a) + ε)) for ε > 0 and af(n/b) ≤ cf(n)
→ T(n) = Θ(f(n))

The Master Theorem provides a quick way to solve divide-and-conquer recurrences without repeated substitution.


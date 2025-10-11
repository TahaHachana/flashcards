## Recurrence Relation to Complexity

What are the three steps to analyze the time complexity of a recursive algorithm?

---

1. **Formulate recurrence relation** T(n): Express running time in terms of T(k) for smaller values k, including base case

2. **Solve recurrence relation**: Use repeated substitution to obtain closed form where T doesn't appear on right side

3. **Apply asymptotic notation**: Express the closed form solution using O, Ω, or Θ notation

Example: T(n) = c + T(n-1) with T(1) = d solves to T(n) = (n-1)c + d = O(n)


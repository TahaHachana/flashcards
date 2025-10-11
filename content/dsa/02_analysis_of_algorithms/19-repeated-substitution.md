## Repeated Substitution Method

Describe the repeated substitution method for solving recurrence relations. What should you do if you can't get an exact sum?

---

**Steps**:
1. Replace T(k) on right side with the recurrence relation itself
2. Adjust parameters appropriately
3. Continue substituting until reaching base case
4. Sum any resulting series (arithmetic, geometric, etc.)
5. If exact sum unavailable, find an upper bound

**If no exact sum**: Work to obtain a close upper bound on the sum, which acts as an upper bound for T(n). This is acceptable for Big O analysis.


## Recursion Requirements

What two properties must any valid recursive procedure satisfy to avoid infinite loops?

---

1. **Base Case(s)**: One or more criteria where the procedure does not call itself (directly or indirectly)

2. **Progress**: Each recursive call must move closer to the base case

Without these, the recursion would never terminate. Example: factorial has base case (n=1) and progresses by calling factorial(n-1), moving toward base case.


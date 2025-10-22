## Recursion Definition

What is recursion and what two properties must a valid recursive function satisfy?

---

Recursion is when a function calls itself, either directly or indirectly.

Two required properties:
1. Base case(s): Condition(s) where the function does not recurse, preventing infinite loops
2. Progress toward base case: Each recursive call must move closer to the base case with a smaller or simpler problem

Without these properties, the recursion will run infinitely or fail.


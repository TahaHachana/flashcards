## Analyzing Nested Loops

How do you determine the time complexity of nested loops?

---

For nested loops, multiply the number of iterations:
- Single loop from 1 to n: O(n)
- Two nested loops, each 1 to n: O(n) × O(n) = O(n²)
- Three nested loops, each 1 to n: O(n) × O(n) × O(n) = O(n³)

For sequential (non-nested) loops, add the complexities:
- Loop 1 to n, then another loop 1 to n: O(n) + O(n) = O(n)

General rule: Nested loops multiply, sequential operations add.


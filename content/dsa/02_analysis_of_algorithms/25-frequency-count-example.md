## Frequency Count Example

For a loop "for i = 1 to n do sum = sum + i end", calculate the total frequency count and derive the Big O complexity.

---

Line-by-line frequency count:
- sum = 0: executed 1 time (before loop)
- for i = 1 to n: loop test executed (n + 1) times
- sum = sum + i: executed n times
- end: executed n times

Total frequency count: 1 + (n + 1) + n + n = 3n + 2

Big O complexity: O(3n + 2) = O(n) after dropping constants and lower-order terms.


## Array Access Time Complexity

Why is array access by index O(1) constant time, and what is this property called?

---

Array access is O(1) because:
1. Elements are stored contiguously in memory
2. We can calculate any element's address directly using the formula: Address = α + (i - l)
3. No need to traverse previous elements

This property is called "random access" or "direct access."

The address calculation involves only arithmetic operations (addition, multiplication) which take constant time, regardless of array size or element position.


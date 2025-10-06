## Loop Analysis

How do we analyze loops in algorithms?

---

- **Simple loop**: iterations × cost per iteration.  
- **Nested loops**: multiply complexities.  

Example:

```c
for (i=0; i<n; i++)      // O(n)
  for (j=0; j<n; j++)    // O(n)
    A[i][j] = 0;         // O(1)
// Total: O(n^2)
```

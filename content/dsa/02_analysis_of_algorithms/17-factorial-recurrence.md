## Factorial Recurrence Analysis

Derive the time complexity of the recursive factorial function from its recurrence relation T(n) = c + T(n-1), T(1) = d.

---

**Solution by repeated substitution**:
```
T(n) = c + T(n-1)
     = c + (c + T(n-2)) = 2c + T(n-2)
     = 3c + T(n-3)
     ...
     = kc + T(n-k)
```

When k = n-1:
```
T(n) = (n-1)c + T(1)
     = (n-1)c + d
     = O(n)
```

**Result**: Linear time complexity despite being recursive.


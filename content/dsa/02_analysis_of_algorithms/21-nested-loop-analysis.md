## Nested Loop Analysis Example

For a nested loop where outer loop runs n times and inner loop runs from 1 to outer loop index, what is the frequency count and time complexity?

---

**Pattern**:
```
for j = 1 to n do
    for k = 1 to j do
        statement
    end
end
```

**Inner statement executes**:
Σ(j=1 to n) j = n(n+1)/2 times

**Frequency count**: n²/2 + n/2 + (other terms)

**Time Complexity**: O(n²) - quadratic, because only highest order term (n²) matters


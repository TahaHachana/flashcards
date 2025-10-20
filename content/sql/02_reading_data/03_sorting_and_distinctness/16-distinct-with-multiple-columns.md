## DISTINCT With Multiple Columns

What happens when you use DISTINCT with multiple columns? Give an example.

---

DISTINCT finds unique combinations of ALL selected columns.

```sql
SELECT DISTINCT state, city
FROM customers;
```

Returns unique (state, city) pairs:
```
state | city
------|-------------
CA    | Los Angeles
CA    | San Diego    ← Same state, different city = unique
NY    | New York
NY    | Buffalo      ← Same state, different city = unique
TX    | Houston
```

Not distinct states, not distinct cities, but distinct COMBINATIONS.

Example:
- (CA, Los Angeles) appears once
- (CA, San Diego) appears once (even though CA repeats)
- (NY, New York) appears once
- (NY, Buffalo) appears once (even though NY repeats)

Each unique pairing appears only once in results.


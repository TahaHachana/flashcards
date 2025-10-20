## Text Numbers Sort Wrong

Why do numbers stored as text sort incorrectly? Show an example.

---

Text sorts character-by-character alphabetically, not numerically.

As TEXT:
```sql
ORDER BY quantity_as_text
```
Result: '1', '10', '100', '2', '20', '5', '50'

Why: Compares character by character:
- '1' < '2' (correct)
- But '10' < '2' (because '1' < '2' in first position)
- '100' < '2' (because '1' < '2' in first position)

As INT:
```sql
ORDER BY quantity_as_int
```
Result: 1, 2, 5, 10, 20, 50, 100 (correct!)

Why: Compares numerical magnitude.

This is a critical reason to use correct data types!

Fix: Store numbers as numeric types (INT, DECIMAL), not TEXT/VARCHAR.


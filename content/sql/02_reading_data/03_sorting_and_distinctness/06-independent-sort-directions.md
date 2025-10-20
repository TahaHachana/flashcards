## Independent Sort Directions

Can each column in ORDER BY have its own sort direction? Give an example.

---

Yes! Each column can be ASC or DESC independently.

```sql
ORDER BY last_name ASC, first_name DESC
```

This means:
- Sort last_name ascending (A-Z)
- Within same last_name, sort first_name descending (Z-A)

Example result:
```
last_name  | first_name
-----------|------------
Anderson   | Bob        ← Anderson's sorted Z-A
Anderson   | Alice
Smith      | Frank      ← Smith's sorted Z-A
Smith      | Emma
Smith      | David
```

Common pattern:
```sql
-- Highest rated first, then by price (cheapest to most expensive):
ORDER BY rating DESC, price ASC
```

Each column's direction is independent.


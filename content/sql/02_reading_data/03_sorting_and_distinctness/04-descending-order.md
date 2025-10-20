## Descending Order

How do you sort in descending order? What does descending mean for different data types?

---

Use DESC keyword for descending order:

```sql
ORDER BY price DESC
```

Descending means:
- Numbers: Largest to smallest (100, 10, 3, 2, 1)
- Text: Reverse alphabetical (Z, Y, X... A)
- Dates: Newest to oldest (2024, 2021, 2020)

Examples:
```sql
-- Most expensive products first:
ORDER BY price DESC

-- Reverse alphabetical:
ORDER BY last_name DESC

-- Newest orders first:
ORDER BY order_date DESC
```

DESC must be explicit - there's no default for descending.


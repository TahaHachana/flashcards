## Sorting By Calculated Columns

Can you sort by calculated columns? Show two approaches.

---

Yes! Two ways:

1. Repeat the calculation:
```sql
SELECT first_name, price, quantity,
       price * quantity AS total
FROM order_items
ORDER BY price * quantity DESC;
```

2. Use the alias (cleaner):
```sql
SELECT first_name, price, quantity,
       price * quantity AS total
FROM order_items
ORDER BY total DESC;
```

Why alias works:
Processing order:
1. SELECT creates the `total` alias
2. ORDER BY runs after SELECT, so sees the alias

Using alias is cleaner and more maintainable (no repeated calculation).

This sorts by the calculated total, most expensive first.


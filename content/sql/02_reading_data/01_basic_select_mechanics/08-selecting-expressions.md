## Selecting Expressions

Can you SELECT things other than column names? Give examples.

---

Yes! You can SELECT:

1. Literal values:
```sql
SELECT 'Hello', 42, 3.14;
```

2. Calculations:
```sql
SELECT price * quantity FROM order_items;
```

3. Function calls:
```sql
SELECT UPPER(name) FROM customers;
```

4. Combined expressions:
```sql
SELECT price * quantity * 1.08 AS total_with_tax FROM orders;
```

Result: Each expression creates a column in the result set (exists only in result, not in table).


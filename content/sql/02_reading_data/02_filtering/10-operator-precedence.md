## Operator Precedence

What is the precedence order for logical operators? Why does this matter?

---

Precedence (highest to lowest):
1. Parentheses ()
2. NOT
3. AND
4. OR

Without parentheses:
```sql
WHERE country = 'USA' OR country = 'Canada' AND age >= 18
```

Evaluates as:
```sql
WHERE country = 'USA' OR (country = 'Canada' AND age >= 18)
```

Result: All USA customers (any age) + Canadian customers 18+

This is probably NOT what you wanted!

With parentheses (explicit):
```sql
WHERE (country = 'USA' OR country = 'Canada') AND age >= 18
```

Result: USA or Canadian customers who are 18+

Best practice: Always use parentheses when mixing AND/OR, even if you know the precedence.


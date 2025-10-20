## SQL is Declarative

What does it mean that SQL is "declarative" rather than "procedural"? Give an example.

---

Declarative: You describe WHAT you want, not HOW to get it
Procedural: You specify exact steps to retrieve data

Example comparison:

Procedural (like Python):
```python
for customer in customers:
    if customer.age >= 18:
        print(customer.name)
```

Declarative (SQL):
```sql
SELECT name FROM customers WHERE age >= 18;
```

Why this matters:
1. You describe the result you want
2. Database decides HOW to retrieve it efficiently
3. No need to specify loops, conditions, or algorithms
4. Same query can be optimized differently based on data/indexes


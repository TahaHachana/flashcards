## Column Order Independence

Can you select columns in a different order than they're defined in the table? Give an example.

---

Yes! Column order in SELECT is independent of table definition.

Table definition: id, first_name, last_name, email

Valid SELECT:
```sql
SELECT email, last_name, first_name FROM customers;
```

Result has columns in the order you specified: email, last_name, first_name

Why this matters:
- Flexibility in presenting data
- Can organize output logically for users
- Order in result set ≠ order in table


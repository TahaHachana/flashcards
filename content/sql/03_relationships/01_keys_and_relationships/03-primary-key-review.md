## Primary Key Review

Review: What are the four essential properties of a primary key?

---

1. Must be UNIQUE - No two rows have the same value
2. Cannot be NULL - Every row must have a value
3. Should not CHANGE - Once assigned, stays the same
4. Should be MEANINGLESS - Best practice: arbitrary IDs

Example:
```
customer_id (PK) | name
-----------------|------------
1                | Alice
2                | Bob
3                | Carol
```

Good: customer_id (surrogate key)
Problematic: email (can change), name (not unique)


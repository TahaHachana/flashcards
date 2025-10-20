## Multi-Column Sort Direction

In `ORDER BY last_name, first_name DESC`, which column sorts descending?

---

Only first_name sorts descending!

```sql
ORDER BY last_name, first_name DESC
```

Means:
- last_name: ascending (default)
- first_name: descending (explicit DESC)

Each column's direction applies only to that column.

Example result:
```
last_name  | first_name
-----------|------------
Anderson   | Zoe        ← Andersons sorted Z-A
Anderson   | Bob
Smith      | Xavier     ← Smiths sorted Z-A  
Smith      | Alice
```

To make both descending:
```sql
ORDER BY last_name DESC, first_name DESC
```

To make both explicit:
```sql
ORDER BY last_name ASC, first_name ASC
```

Direction must be specified for each column you want to control.


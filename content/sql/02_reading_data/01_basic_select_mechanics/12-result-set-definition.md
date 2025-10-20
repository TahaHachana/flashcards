## Result Set Definition

What is a result set? What are its properties?

---

A result set is a temporary table containing data returned by a SELECT query.

Properties:
- It's a table (rows and columns)
- It's temporary (exists only for your query)
- It's not stored in the database
- Each row represents data meeting your criteria
- Columns are what you specified in SELECT

Example result set:
```
first_name | age
-----------|-----
Alice      | 25
Bob        | 30
Carol      | 21
```

Key insight: Result sets are tables. This matters because many SQL operations work on tables, so you can treat result sets like tables.


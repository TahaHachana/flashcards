## Selecting All Columns

How do you select all columns from a table, and why should this be used cautiously?

---

Use the asterisk (`*`) wildcard:  
`SELECT * FROM table_name;`  
It’s convenient for exploration but discouraged in production because it can return unnecessary data, slow performance, and cause maintenance issues.


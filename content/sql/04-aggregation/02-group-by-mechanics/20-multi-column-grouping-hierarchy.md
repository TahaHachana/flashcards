## Multi Column Grouping Hierarchy

When using multi-column grouping, what is the recommended practice for column order, and why?

---

Best practice: arrange columns in logical hierarchical order from broader to narrower (e.g., GROUP BY country, state, city rather than city, state, country). This makes queries more readable and matches how humans think about nested categories. While it doesn't change the groups created, it improves code clarity and may help query optimization.


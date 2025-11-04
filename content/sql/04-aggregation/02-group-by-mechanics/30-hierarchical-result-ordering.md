## Hierarchical Result Ordering

When grouping by multiple columns like `GROUP BY region, store, product`, what ORDER BY pattern typically makes results most readable?

---

ORDER BY the same columns in the same hierarchical order: ORDER BY region, store, product. This creates a nested structure where results are organized by region, then within each region by store, then within each store by product. This hierarchical ordering matches the grouping structure and makes it easy to scan results by scanning down through the hierarchy levels.


## Example with Both Clauses

Given: "Show California customers who have spent more than $1000 total." Which parts go in WHERE and which in HAVING?

---

WHERE state = 'CA' (filters to California customers before grouping), GROUP BY customer_id (creates groups), HAVING SUM(amount) > 1000 (filters groups to those with total spending over $1000). WHERE filters rows based on state, HAVING filters groups based on aggregate spending. Both are necessary for the correct logic.


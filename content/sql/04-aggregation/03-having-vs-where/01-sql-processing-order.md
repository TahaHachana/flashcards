## SQL Processing Order

What is the complete SQL processing order, and why does it matter for understanding WHERE vs HAVING?

---

The order is: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. This matters because WHERE is evaluated before grouping (filters rows), while HAVING is evaluated after grouping (filters groups). WHERE happens before aggregates are calculated, HAVING happens after. This timing determines what each clause can access and filter on.


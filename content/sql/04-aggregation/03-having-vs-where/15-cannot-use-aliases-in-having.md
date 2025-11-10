## Cannot Use Aliases in HAVING

Why can't you use column aliases in the HAVING clause?

---

HAVING is processed before SELECT, so aliases don't exist yet. Example: SELECT customer_id, COUNT(*) AS num_orders ... HAVING num_orders > 10 fails because num_orders isn't created until SELECT runs (which happens after HAVING). You must repeat the expression: HAVING COUNT(*) > 10. This is the same reason you can't use aliases in GROUP BY.


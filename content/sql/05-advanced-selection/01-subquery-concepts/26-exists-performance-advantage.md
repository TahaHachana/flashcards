## EXISTS Performance Advantage

What performance advantage does EXISTS have over other approaches?

---

Short-circuit evaluation: EXISTS often stops searching as soon as it finds one matching row, making it faster than counting or selecting all matching rows.

Comparison:
- COUNT(*): Must scan all matching rows to get the count
- EXISTS: Can stop after finding the first match

Example - Both find customers with rentals, but EXISTS is faster:

Slower (must count all):
WHERE 0 < (SELECT COUNT(*) FROM rental r WHERE r.customer_id = c.customer_id)

Faster (stops at first match):
WHERE EXISTS (SELECT 1 FROM rental r WHERE r.customer_id = c.customer_id)

Best for "does this relationship exist?" questions.


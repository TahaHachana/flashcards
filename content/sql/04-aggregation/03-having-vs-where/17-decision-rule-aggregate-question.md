## Decision Rule Aggregate Question

What is the primary decision rule for choosing between WHERE and HAVING?

---

Ask: "Does this condition involve an aggregate function (COUNT, SUM, AVG, MIN, MAX)?" If YES → use HAVING (aggregates exist after grouping). If NO → probably use WHERE (more efficient to filter before grouping). Examples: COUNT(*) > 10 requires HAVING, state = 'CA' should use WHERE.


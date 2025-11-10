## Processing Without GROUP BY

If a query has WHERE and SELECT with aggregates but no GROUP BY, what happens?

---

There's implicit grouping (one group containing all rows). Process: FROM gets data, WHERE filters rows, implicit GROUP BY creates one group with all filtered rows, aggregates calculate on that single group, SELECT returns one row with aggregate results. Example: SELECT COUNT(*) FROM orders WHERE status = 'completed' returns one row with the count of completed orders.


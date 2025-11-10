## What Data is Available at WHERE

What data is available when WHERE is evaluated, and what is NOT available?

---

Available: Raw row data from tables, column values from individual rows. NOT available: Groups (don't exist yet), aggregate values (haven't been calculated), column aliases from SELECT (SELECT hasn't run yet). WHERE can only work with row-level data that exists before any grouping or aggregation.


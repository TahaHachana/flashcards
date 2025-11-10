## What Data is Available at HAVING

What data is available when HAVING is evaluated?

---

Available: Groups (already created), aggregate values (already calculated), raw row data for grouped columns. NOT available: Column aliases from SELECT (SELECT happens after HAVING). HAVING can filter on aggregate functions like COUNT, SUM, AVG because these have been calculated by the time HAVING runs.


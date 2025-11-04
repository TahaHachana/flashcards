## Aggregates Change Grain

What does it mean that "aggregates change the grain of your data"?

---

Aggregates transform data from row-level detail (individual records) to summary-level statistics (calculated values across multiple rows). For example, a payment table with 16,049 individual payment rows (row-level grain) becomes a single row showing total revenue (summary-level grain) when you use SUM(amount). The level of detail fundamentally changes from specific to general.


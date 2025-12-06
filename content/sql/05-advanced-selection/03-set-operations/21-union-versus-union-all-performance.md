## UNION Versus UNION ALL Performance

What are the performance differences between UNION and UNION ALL, and when should you choose each?

---

UNION:
- Must check for duplicates across entire combined result set
- May sort results (database-dependent)
- More memory intensive
- Slower, especially on large datasets

UNION ALL:
- No duplicate checking
- No sorting
- Simply appends result sets
- MUCH faster for large datasets

Performance comparison (hypothetical):
- 1M rows UNION 1M rows: ~10 seconds
- 1M rows UNION ALL 1M rows: ~2 seconds

When to use UNION:
- You specifically need duplicates removed
- Result set is small (performance difference negligible)
- Correctness requires deduplication

When to use UNION ALL (default choice):
- You know duplicates don't exist
- You want to keep duplicates
- Performance matters
- Being explicit about keeping all rows

Best practice: Default to UNION ALL unless you specifically need deduplication. It's faster and more explicit about intent.

Rule of thumb: If you're unsure whether duplicates exist, profile with both and see if UNION removes any rows. If it doesn't, use UNION ALL.


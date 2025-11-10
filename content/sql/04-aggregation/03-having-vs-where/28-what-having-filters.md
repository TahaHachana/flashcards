## What HAVING Filters

What does HAVING filter - rows or groups? Explain the difference.

---

HAVING filters groups, not individual rows. After GROUP BY creates groups (like one per customer), HAVING decides which entire groups to keep or discard based on their aggregate values. Example: HAVING COUNT(*) > 10 removes entire customer groups (all their rows) if that customer has 10 or fewer orders. WHERE filters individual rows; HAVING filters entire groups of rows.


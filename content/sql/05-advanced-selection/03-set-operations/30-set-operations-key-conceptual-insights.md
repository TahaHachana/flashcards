## Set Operations Key Conceptual Insights

What are the three most important conceptual insights about set operations?

---

1. Set operations combine rows vertically, JOINs combine columns horizontally
   - Set operations: Stack result sets (more rows, same columns)
   - JOINs: Merge tables side-by-side (same rows, more columns)
   - Fundamentally different operations serving different purposes
   - Choose based on whether you need "more rows" or "more columns"

2. Three operations map directly to set theory
   - UNION: Combination (A + B - duplicates)
   - INTERSECT: Overlap (only what's in both A and B)
   - EXCEPT: Difference (A minus B)
   - Understanding set theory diagrams helps visualize results
   - Each has specific use cases based on the question being asked

3. Requirements are strict but logical
   - Same number of columns (for alignment)
   - Compatible types (so they can stack)
   - Order matters for columns (position, not name)
   - First query defines names/aliases
   - Sort only the final result, not individual parts

Special insight: UNION ALL is usually better than UNION
   - Faster (no duplicate checking)
   - More explicit about intent
   - Default choice unless deduplication specifically needed

Master these insights and set operations become natural tools for "stacking" data from multiple sources.


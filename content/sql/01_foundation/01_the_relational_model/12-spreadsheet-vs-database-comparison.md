## Spreadsheet vs Database Comparison

Why is storing data like "Order1: Widget ($10), Order2: Gadget ($20)" in a single spreadsheet cell problematic compared to a relational database approach?

---

Spreadsheet approach problems:
1. Multiple values in one cell (violates atomicity)
2. Can't easily answer "How many widgets were sold?"
3. Can't sort orders independently of customers
4. Updating prices requires finding every occurrence

Database approach:
- Separate Orders table with one row per order
- Each piece of information appears once
- Easy to query, sort, and update any entity independently


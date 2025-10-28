## Unintentional Cartesian Product

What causes an unintentional Cartesian product, and what are the warning signs?

---

An unintentional Cartesian product occurs when you forget the JOIN condition (ON clause) or write an incorrect/too-broad condition that matches many rows. Warning signs include: (1) unexpectedly large result sets, (2) duplicate data appearing multiple times, (3) row counts equal to the product of the table sizes, and (4) slow query performance.


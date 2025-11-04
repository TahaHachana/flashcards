## Column Order in GROUP BY

Does the order of columns in GROUP BY affect what groups are created? Does `GROUP BY state, city` produce different groups than `GROUP BY city, state`?

---

No, the order does not affect what groups are created. Both produce identical groups - one group per unique (state, city) combination. However, the order may affect query performance and makes queries more readable when following logical hierarchies (broader to narrower). Best practice: use hierarchical order like GROUP BY country, state, city.


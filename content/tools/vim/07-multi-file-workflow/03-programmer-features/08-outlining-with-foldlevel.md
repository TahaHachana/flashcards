## Outlining With Foldlevel

After `:set foldmethod=indent`, how do you show only top-level headings versus more detail?

---

`:set foldlevel=N` shows only lines whose fold level is ≤ N. A low value (e.g. 0) shows headings; raise it (`zr`) to reveal detail or lower it (`zm`) to collapse.


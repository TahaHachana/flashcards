## Swap Two Fields With awk

What awk program, used as a filter, swaps the first two fields of every line?

---

`awk '{print $2, $1}'`


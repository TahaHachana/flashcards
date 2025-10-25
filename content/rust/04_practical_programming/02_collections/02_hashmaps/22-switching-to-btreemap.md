## Switching to BTreeMap

What changes are needed to convert HashMap code to use BTreeMap?

---

Usually just two changes:
1. Change the import: `use std::collections::BTreeMap;`
2. Change the type: `BTreeMap::new()` instead of `HashMap::new()`

Methods like `.insert()`, `.get()`, `.entry()` work identically. Iteration will now be in sorted order.


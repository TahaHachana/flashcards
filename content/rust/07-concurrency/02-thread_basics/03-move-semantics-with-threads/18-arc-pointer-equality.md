## Arc Pointer Equality

If you create multiple Arc clones, are they pointing to the same data or different copies?

---

Same data. Arc::clone creates new pointers to the same underlying data, not copies of the data. You can verify: Arc::ptr_eq(&arc1, &arc2) returns true. Only one allocation exists for the data, multiple Arc handles reference it. This is why Arc::clone is cheap and why all threads see the same data. When all Arc handles are dropped, the data is freed.


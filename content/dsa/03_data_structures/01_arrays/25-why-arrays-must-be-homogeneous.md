## Why Arrays Must Be Homogeneous

Why must all elements in a static array be of the same data type?

---

Arrays require homogeneous elements (same data type) for three reasons:

1. Memory allocation - Compiler needs to know exactly how much space to allocate
2. Address calculation - Formula depends on uniform element size
   - Address = base + index × element_size
   - If sizes varied, direct calculation would be impossible
3. Performance optimization - Enables O(1) random access

If element sizes differed, we'd need to traverse from the beginning to find each element (O(n) access time), defeating the purpose of arrays.

Some languages (like Python) relax this requirement but sacrifice some performance benefits.


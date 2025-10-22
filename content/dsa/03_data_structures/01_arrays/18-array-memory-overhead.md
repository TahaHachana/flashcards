## Array Memory Overhead

What is the memory overhead for an array A[1:n] storing elements of a given data type?

---

For array A[1:n]:

Memory required:
- n × (size of data type) for the elements
- Plus: pointer to base address (4 or 8 bytes typically)

No per-element overhead:
- Unlike linked structures, arrays don't store pointers with each element
- Just the raw data in contiguous locations

This minimal overhead makes arrays very memory-efficient for storing collections.


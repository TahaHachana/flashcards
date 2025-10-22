## Sparse Matrix Problem and Solution

What is a sparse matrix, what problem does it create, and how is it solved efficiently?

---

Sparse matrix: A matrix where most elements are zero.

Problem: Storing a 1000×1000 sparse matrix with only 100 non-zero elements wastes 999,900 memory locations!

Solution: Use 3-tuple representation
- Store only non-zero elements as (row, column, value) triplets
- First row stores matrix metadata: (rows, columns, count of non-zeros)
- Subsequent rows store each non-zero element

Benefit: Stores only meaningful data, reducing memory usage dramatically.


## Row-Major vs Column-Major Order

What is the difference between row-major order and column-major order for storing multidimensional arrays in memory?

---

Row-major order: Store complete rows sequentially in memory
- Used by: C, C++, Java
- Example: For 2×3 array, store: Row1[all columns], then Row2[all columns]

Column-major order: Store complete columns sequentially in memory
- Used by: Fortran, MATLAB
- Example: For 2×3 array, store: Col1[all rows], then Col2[all rows], etc.

Computer memory is one-dimensional, so we need a systematic way to map multi-dimensional structures to linear memory.


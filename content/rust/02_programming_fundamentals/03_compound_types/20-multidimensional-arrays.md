## Multidimensional Arrays

How do you create and access multidimensional arrays?

---

Nest arrays and use multiple indices.

```rust
let matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
let element = matrix[1][2];  // 6
let grid: [[i32; 3]; 3] = matrix;
```


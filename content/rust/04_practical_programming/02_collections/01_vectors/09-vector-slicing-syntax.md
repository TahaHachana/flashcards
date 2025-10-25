## Vector Slicing Syntax

Given `let v = vec![0,1,2,3,4,5];`, what do these slices return?
- `&v[2..5]`
- `&v[..3]`
- `&v[2..]`
- `&v[2..=4]`

---

- `&v[2..5]` → `[2, 3, 4]` (indices 2,3,4 - exclusive end)
- `&v[..3]` → `[0, 1, 2]` (start to index 2)
- `&v[2..]` → `[2, 3, 4, 5]` (index 2 to end)
- `&v[2..=4]` → `[2, 3, 4]` (indices 2,3,4 - inclusive end)


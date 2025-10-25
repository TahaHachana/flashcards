## Clone vs Copy Elements

What happens differently when you iterate with `.into_iter()` over `Vec<i32>` vs `Vec<String>`?

---

`Vec<i32>`: Elements are `Copy`, so even though moved, it's a bitwise copy (cheap).
`Vec<String>`: Elements are not `Copy`, so ownership truly transfers. Each String is moved out. Both consume the vector, but internal behavior differs.


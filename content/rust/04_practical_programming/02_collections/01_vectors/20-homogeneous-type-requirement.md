## Homogeneous Type Requirement

Can you create `vec![1, "hello", 3.14]`? Why or why not?

---

No. All elements in a `Vec<T>` must be the same type. The compiler will reject this. To store different types, use an enum wrapper or trait objects (covered later).


## Vec Generic Constraint

Can you create a `Vec<T>` where T is an unsized type like `str`? Why or why not?

---

No. `Vec<T>` requires `T` to be `Sized` (known size at compile time). You can't have `Vec<str>`, only `Vec<String>` or `Vec<&str>`. The vector needs to know element size for memory layout.


## Vec::new() Requires Type Annotation

Why does `Vec::new()` require a type annotation while `vec![]` often doesn't?

---

`Vec::new()` creates an empty vector with no elements for the compiler to infer the type from, so you must specify it: `Vec::new::<i32>()` or `let v: Vec<i32> = Vec::new();`. With `vec![]`, Rust can infer the type from the initial elements.


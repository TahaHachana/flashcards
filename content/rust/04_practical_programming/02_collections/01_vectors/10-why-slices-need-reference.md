## Why Slices Need Reference

Why do you need `&` when slicing a vector (e.g., `&vec[2..5]` not `vec[2..5]`)?

---

Slices are unsized types (`[T]`) - the compiler doesn't know their size at compile time. The `&` creates a reference which is a fat pointer containing both the data address and the length, making it a sized type the compiler can work with.


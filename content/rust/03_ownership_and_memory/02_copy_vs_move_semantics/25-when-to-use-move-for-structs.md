## When to Use Move for Structs

When should a custom struct use move semantics?

---

When any field allocates (String, Vec, Box), the type manages resources, or you want to enforce single ownership.


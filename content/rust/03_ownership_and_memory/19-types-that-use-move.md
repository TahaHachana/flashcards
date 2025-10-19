## Types That Use Move

What types use move semantics instead of Copy?

---

Types with heap allocation: String, Vec<T>, Box<T>, custom structs containing non-Copy types, and tuples containing any non-Copy type.


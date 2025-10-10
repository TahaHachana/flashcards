## Always Stack Types

Which Rust types are always stored entirely on the stack?

---

Scalar types (i32, u64, f64, bool, char), tuples of stack types, fixed arrays [T; N], and references (&T, &mut T) - though the reference itself is on the stack, not necessarily the data it points to.


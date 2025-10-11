## Choosing Integer Types

What are best practices for choosing integer types?

---

Use i32 by default, u32 when never negative, i64/u64 for large numbers, usize for indices/sizes, and u8 for bytes.


## Vec vs Array Key Differences

What are the three main differences between `Vec<T>` and arrays `[T; N]`?

---

1. **Size**: Arrays have fixed size at compile time; vectors are dynamic and can grow/shrink
2. **Memory**: Arrays on stack (if small); vectors always heap-allocated
3. **Type**: Array size is part of type `[i32; 5]`; vector size is not `Vec<i32>`


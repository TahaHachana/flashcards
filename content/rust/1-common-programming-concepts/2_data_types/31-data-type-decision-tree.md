## Data Type Decision Tree

How can you quickly decide between common Rust types like array, Vec, &str, String, tuple, and struct?

---

Use this step-by-step guide:

1. **Numbers**
    - Default: `i32` for integers, `f64` for floats.
    - Need unsigned? Use `u*`.
    - Need pointer-sized? Use `isize`/`usize`.

2. **Collections**
    - Size fixed at compile time? → **Array `[T; N]`**.
    - Size dynamic at runtime? → **Vec<T>**.

3. **Strings**
    - Borrowed, read-only? → **&str**.
    - Owned, growable, modifiable? → **String**.

4. **Grouping values**
    - Temporary grouping, no names needed? → **Tuple**.
    - Data with meaning, clarity, or public API? → **Struct**.

5. **Return type when nothing**
    - → **Unit `()`**

This tree helps pick the right type based on ownership, size, and purpose.


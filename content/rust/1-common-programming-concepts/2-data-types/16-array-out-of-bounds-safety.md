## Array Out-Of-Bounds Safety

What happens if you access an array index out of bounds in Rust?

---

Rust checks indices at runtime.
If the index ≥ array length, the program panics to prevent invalid memory access.


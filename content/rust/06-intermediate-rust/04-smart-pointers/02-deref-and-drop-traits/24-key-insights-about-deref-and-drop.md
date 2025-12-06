## Key Insights About Deref and Drop

What are the seven key insights about the `Deref` and `Drop` traits?

---

**1. Deref enables transparency:** Smart pointers act like the data they contain while maintaining ownership

**2. Deref coercion is powerful:** Automatic conversions make smart pointers ergonomic to use

**3. Drop enables RAII:** Resources are automatically cleaned up, preventing leaks

**4. They work together:** Deref makes smart pointers easy to use, Drop makes them safe

**5. Use judiciously:** Implement Deref only for pointer-like types to avoid confusion

**6. Drop order matters:** Understanding LIFO drop order is important for complex scenarios

**7. Manual drop when needed:** Use `std::mem::drop()` for early cleanup, but you can't call `.drop()` directly

**Bottom line:** These two traits are what make smart pointers "smart" - they provide both ergonomic access (Deref) and automatic cleanup (Drop) while maintaining Rust's safety guarantees.


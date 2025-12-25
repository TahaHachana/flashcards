## Purpose of Unit Tests in Rust

What runtime issues can unit tests catch that the Rust compiler cannot detect?

---

Unit tests catch runtime issues that compile-time checks miss:
- Logic errors (function returns wrong value)
- Incorrect algorithms (sorting implementation has bugs)
- Business rule violations (validation accepts invalid input)
- Edge cases (code fails on empty inputs or boundary values)

The compiler catches type errors, borrow checker violations, and lifetime issues, but cannot verify that your logic is correct.


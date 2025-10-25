## Why Rule 1 Exists

Why does Rule 1 (exclusive mutable or shared immutable) exist?

---

Prevents data races. Multiple mutable references or mixing mutable with immutable creates situations where code could interfere with itself unpredictably, causing conflicts and bugs.


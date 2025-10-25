## Why Rule 2 Exists

Why does Rule 2 (references must be valid) exist?

---

Prevents use-after-free. If references could outlive their data, you'd access freed memory (undefined behavior). Ensures references always point to valid data.


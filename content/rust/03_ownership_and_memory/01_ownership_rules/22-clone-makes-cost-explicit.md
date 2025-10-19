## Clone Makes Cost Explicit

Why does Rust require explicit .clone() for deep copies?

---

It makes the cost visible - you're deliberately choosing to pay for heap allocation and data copying. Prevents hidden expensive operations.


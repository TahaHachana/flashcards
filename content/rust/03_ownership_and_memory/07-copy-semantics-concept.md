## Copy Semantics Concept

What is Copy semantics and when is it used?

---

For small, stack-only types, assignment creates a duplicate rather than transferring ownership. Used because copying stack data is cheap and safe (no heap allocation, no double-free risk).


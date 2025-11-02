## Reading Lifetime Error Messages

What steps should you take when encountering a lifetime mismatch error?

---

1. Find what lifetimes are involved in the error
2. Identify which parameter's lifetime doesn't match expectations
3. Ask: "Which input does the output actually come from?"
4. Apply the right pattern:
   - Return from multiple inputs → same lifetime
   - Return from one input → tie to that lifetime only
   - Return is independent (e.g., string literal) → use `'static`


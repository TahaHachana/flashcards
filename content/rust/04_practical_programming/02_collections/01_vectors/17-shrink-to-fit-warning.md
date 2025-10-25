## Shrink to Fit Warning

What does `.shrink_to_fit()` do, and what's the gotcha with using it?

---

It reduces capacity to match length, freeing unused memory. **Gotcha**: Adding even one element after shrinking will double the capacity again, potentially wasting the optimization. Only shrink when you're done growing the vector.


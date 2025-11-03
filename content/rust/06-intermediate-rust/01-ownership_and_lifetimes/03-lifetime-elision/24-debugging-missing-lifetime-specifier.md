## Debugging Missing Lifetime Specifier

What steps should you take when you get a "missing lifetime specifier" error?

---

1. Count reference inputs in the function
2. Check if there's output with references
3. Apply elision rules mentally:
   - One input? Rule 2 should work
   - Multiple inputs with &self? Rule 3 should work
   - Multiple inputs without &self? Need explicit annotations
4. If ambiguity remains, add explicit annotations showing which input(s) the output relates to


## Pattern Decision Tree Question 2

Using the pattern decision tree, what pattern applies to a function that takes one slice reference and returns a reference to an element?

---

Pattern 1 (Input-Output Flow, Single Source). The output reference comes from the one input, so they share the same lifetime. Example: `fn first<'a>(data: &'a [i32]) -> &'a i32`. Mental shortcut: "Output points into input" → same lifetime.


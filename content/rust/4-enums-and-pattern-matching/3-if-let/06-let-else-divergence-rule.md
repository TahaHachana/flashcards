## Let Else Divergence Rule

What must the `else` block in a `let else` expression do?

---

The `else` block must **diverge** (e.g., `return`, `break`, or `panic!`).
It cannot continue execution normally.


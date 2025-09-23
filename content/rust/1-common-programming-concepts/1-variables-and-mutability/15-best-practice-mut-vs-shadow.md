## Best Practice: Mut vs Shadow

When is shadowing generally preferred over `mut`?

---

Shadowing is clearer for step-by-step transformations or type changes while keeping the same name.
`mut` is clearer for repeated updates to the same value when the type does not change.


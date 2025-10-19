## When to Use Copy for Structs

When should you make a custom struct Copy?

---

When all fields are small and Copy, the type represents a simple value (coordinates, colors, IDs), and implicit copying is convenient and safe.


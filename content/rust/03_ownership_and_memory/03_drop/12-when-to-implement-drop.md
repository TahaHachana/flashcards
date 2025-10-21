## When to Implement Drop

When should you implement Drop for custom types?

---

When managing resources needing explicit cleanup: file handles, network connections, locks, database connections, or external resources. Not for simple data or types wanting Copy.


## Iter Ownership and Collection State

After calling each iterator method, can you still use the original collection?

---

- `.iter()`: ✅ Yes, collection still exists (borrowed immutably)
- `.iter_mut()`: ✅ Yes, collection still exists (borrowed mutably)
- `.into_iter()`: ❌ No, collection was consumed (moved)

Example: After `vec.into_iter()`, you cannot use `vec` anymore.


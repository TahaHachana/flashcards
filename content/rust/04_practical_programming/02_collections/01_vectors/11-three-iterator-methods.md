## Three Iterator Methods

Explain the difference between `.iter()`, `.iter_mut()`, and `.into_iter()` on vectors.

---

- `.iter()`: Borrows immutably, yields `&T`, vector still usable after
- `.iter_mut()`: Borrows mutably, yields `&mut T`, can modify elements
- `.into_iter()`: Consumes vector, yields `T` (owned values), vector no longer exists after


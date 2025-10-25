## Three Iterator Methods Overview

What are the three core iterator methods in Rust and what does each return?

---

- `.iter()` → Returns `&T` (immutable references), borrows collection
- `.iter_mut()` → Returns `&mut T` (mutable references), borrows mutably
- `.into_iter()` → Returns `T` (owned values), consumes collection

After `.into_iter()`, the collection is gone. After `.iter()` or `.iter_mut()`, it still exists.


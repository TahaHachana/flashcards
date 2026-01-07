## Arc Clone Mechanics

When you call Arc::clone(&arc), what gets cloned and what doesn't?

---

Arc::clone clones the Arc pointer and increments the atomic reference count - it does NOT clone the underlying data. All Arc clones point to the same data in memory. This is cheap (just an atomic increment) compared to cloning the actual data. Example: Arc::new(vec![1,2,3]) with 3 clones = 1 Vec in memory, 3 Arc pointers to it, reference count = 3.


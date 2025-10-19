## Why No Manual Free

Why doesn't Rust require manual memory deallocation like C?

---

The ownership system automatically frees memory when the owner goes out of scope via Drop. The compiler tracks ownership, so it knows exactly when to clean up. No manual free needed.


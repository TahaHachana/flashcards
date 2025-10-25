## Slices Complete Ownership Story

How do slices complete Rust's ownership model?

---

You can own data (String, Vec), borrow all of it (&String, &Vec), or borrow part of it (&str, &[T]). This flexibility with compiler-enforced safety makes the memory model powerful and practical.


## Why Copy vs Move Distinction

Why does Rust have different behavior for Copy vs Move types?

---

Copying integers is cheap (just a few bytes). Copying heap data is expensive (allocate and copy all data). Move prevents expensive copies and double-free bugs. The compiler enforces this automatically.


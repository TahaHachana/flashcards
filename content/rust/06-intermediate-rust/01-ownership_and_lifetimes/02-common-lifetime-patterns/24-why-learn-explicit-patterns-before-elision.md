## Why Learn Explicit Patterns Before Elision

Why is it important to understand explicit lifetime patterns before learning lifetime elision?

---

Understanding explicit patterns helps you recognize what the compiler is doing automatically when it elides lifetimes. You can contrast "here's the verbose way" (explicit annotations) vs "here's what the compiler infers" (elision). This makes elision feel like a reward—a shorthand for patterns you already understand—rather than confusing magic. It also helps you debug elision edge cases where you need explicit annotations.


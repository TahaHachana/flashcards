## Three Core Organizational Concepts in Rust

What are the three fundamental concepts Rust uses to organize code, listed from largest to smallest?

---

1. **Package** - A Cargo feature that lets you build, test, and share crates
2. **Crate** - A compilation unit (the smallest amount of code the compiler considers at a time)
3. **Module Tree** - The internal organization structure within a crate

The hierarchy: Package → Crate(s) → Module Tree → Individual modules


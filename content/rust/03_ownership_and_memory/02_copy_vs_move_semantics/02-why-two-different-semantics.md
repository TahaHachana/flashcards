## Why Two Different Semantics

Why does Rust have both copy and move semantics?

---

Performance (copying large data is expensive), safety (move prevents double-free by ensuring one owner), and ergonomics (small types like integers should be usable naturally).


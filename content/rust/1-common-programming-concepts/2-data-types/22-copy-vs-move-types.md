## Copy vs Move Types

Which types implement `Copy` in Rust, and which don’t?

---

**Copy types**: cheap to duplicate; ownership doesn’t move. Examples: integers, floats, bool, char, unit `()`.

**Non-Copy types**: ownership moves by default. Examples: `String`, `Vec<T>`, `Box<T>`.


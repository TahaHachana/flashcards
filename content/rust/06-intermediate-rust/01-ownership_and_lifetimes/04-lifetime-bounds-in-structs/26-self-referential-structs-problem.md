## Self-Referential Structs Problem

Why can't you safely create a struct that holds a reference to its own data in safe Rust?

---

Because moving the struct would invalidate the reference:
```rust
// ❌ Can't do this safely
struct SelfRef {
    data: String,
    slice: &str,  // Would reference self.data
}
```
If the struct moves in memory, `slice` would point to the old location. Solutions: Use `Pin` with unsafe code (advanced), use specialized crates (`rental`, `ouroboros`), or redesign to avoid self-references (usually best).


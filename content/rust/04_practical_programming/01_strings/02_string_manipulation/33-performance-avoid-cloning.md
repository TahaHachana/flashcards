## Performance - Avoid Cloning

Why is slicing more efficient than cloning when passing strings to functions?

---

```rust
// Slow: copies entire string
fn process(s: String) { }
let s = long_string.clone();
process(s);

// Fast: just borrows
fn process(s: &str) { }
process(&long_string);
```
Slicing creates a borrowed view (pointer + length) with no copying. Cloning allocates new heap memory and copies all data.


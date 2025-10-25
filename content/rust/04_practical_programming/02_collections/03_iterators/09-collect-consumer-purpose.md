## Collect Consumer Purpose

What does `.collect()` do and why does it often need type annotations?

---

`.collect()` consumes an iterator and gathers items into a collection (Vec, HashMap, etc.).

Needs type annotation because it can build many types:
```rust
let vec: Vec<i32> = iter.collect();
// or
let vec = iter.collect::<Vec<i32>>();
```


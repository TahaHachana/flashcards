## Copy Types

What are Copy types in Rust, and how do they differ from move semantics?

---

Copy types are duplicated instead of moved.
They are usually simple, fixed-size values stored on the stack:

* integers, floats, booleans, chars, and tuples of Copy types.

```rust
let x = 5;
let y = x; // both valid, Copy occurs
```


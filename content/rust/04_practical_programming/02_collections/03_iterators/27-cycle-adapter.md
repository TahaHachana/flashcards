## Cycle Adapter

What does `.cycle()` create and when should you use it carefully?

---

Creates an infinite iterator that repeats forever:
```rust
let cycle = ["a", "b"].iter().cycle();
// a, b, a, b, a, b, ... forever

// Use with .take() to limit:
let limited: Vec<&str> = cycle.take(5).collect();
// ["a", "b", "a", "b", "a"]
```
**Warning**: Without `.take()` or similar, will loop forever!


## Map Adapter Purpose

What does `.map()` do and is it lazy?

---

`.map()` applies a function to each item and passes it on to create a new iterator.

**Yes, it's lazy** - nothing happens without `.collect()` or similar:
```rust
let doubled: Vec<i32> = vec.iter()
    .map(|x| x * 2)  // Transform each item
    .collect();      // Actually execute
```


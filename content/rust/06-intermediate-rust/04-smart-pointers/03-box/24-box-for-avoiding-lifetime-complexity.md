## Box for Avoiding Lifetime Complexity

How can `Box` help avoid complex lifetime annotations in structs that hold data?

---

`Box` owns its data, so you don't need lifetime parameters for the data it contains.

**Without Box (requires lifetime):**
```rust
// ❌ Complex: needs lifetime parameter
struct Container<'a> {
    data: &'a str,
}

// Must track where data comes from
fn create<'a>(s: &'a str) -> Container<'a> {
    Container { data: s }
}
```

**With Box (no lifetime needed):**
```rust
// ✅ Simple: Box owns the data
struct Container {
    data: Box<str>,
}

fn create(s: &str) -> Container {
    Container {
        data: s.to_string().into_boxed_str(),
    }
}
```

**Trade-off:**
- Without Box: No allocation, but lifetime complexity
- With Box: Heap allocation, but simpler lifetimes

**Use when:** Lifetime annotations become too complex, and allocation cost is acceptable.

**Note:** This is a trade-off - you're exchanging compile-time complexity for runtime allocation cost.


## Pattern 4 Cache Structs

What is the cache/lookup pattern with lifetimes, and what's its key characteristic?

---

A struct that holds a collection of references, where all references share the same lifetime tied to the source data. Example:
```rust
struct Cache<'a> {
    entries: Vec<&'a str>,
}
```
The cache doesn't own the data—it holds references to data owned elsewhere. The struct's lifetime is constrained by the lifetime of that source data.


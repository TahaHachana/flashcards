## Zero Cost Abstractions

What are "zero-cost abstractions" in the context of iterators?

---

High-level iterator code compiles to the same efficiency as low-level loops:
```rust
// This elegant code:
vec.iter().map(|x| x * 2).collect()

// Compiles as fast as:
let mut result = Vec::new();
for x in &vec {
    result.push(x * 2);
}
```
No performance penalty for abstraction!


## Zero-Cost Abstractions Example

How do iterators demonstrate zero-cost abstractions?

---

High-level iterator code compiles to the same machine code as manual loops:

```rust
// High-level
let sum: i32 = vec.iter().filter(|&x| x % 2 == 0).sum();

// Compiles to same code as manual loop
let mut sum = 0;
for i in 0..vec.len() {
    if vec[i] % 2 == 0 { sum += vec[i]; }
}
```


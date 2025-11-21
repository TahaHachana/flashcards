## Iterator Performance and Zero Cost

Why are Rust iterators called "zero-cost abstractions"? How do they compare to manual loops?

---

Iterator chains compile down to the same efficient machine code as hand-written loops, with no runtime overhead.

**Zero-cost abstraction means:**
1. No runtime overhead (speed)
2. No extra memory allocation
3. Compiler optimizations apply equally
4. Abstractions don't cost performance

**Example comparison:**

**Manual loop:**
```rust
let mut sum = 0;
for &num in numbers.iter() {
    if num % 2 == 0 {
        sum += num * num;
    }
}
```

**Iterator chain:**
```rust
let sum: i32 = numbers.iter()
    .filter(|&&x| x % 2 == 0)
    .map(|&x| x * x)
    .sum();
```

**Both compile to identical assembly code!**

**How this works:**

1. **Inlining:** Closures and iterator methods inline
2. **Monomorphization:** Generic code specialized at compile time
3. **Dead code elimination:** Unused branches removed
4. **Loop fusion:** Multiple operations merge into single pass

**Iterator advantages:**
- Same performance as loops
- More readable and composable
- Harder to write bugs (no off-by-one errors)
- Compiler checks correctness

**Performance tips:**
```rust
// Good - single pass
iter.filter(...).map(...).sum()

// Good - lazy, only processes what's needed
iter.take(10).map(expensive_operation)

// Good - no allocations until collect()
iter.filter(...).map(...).collect()
```

**Myth busted:** "Functional style is slow in Rust" - FALSE! It's exactly as fast as imperative loops.


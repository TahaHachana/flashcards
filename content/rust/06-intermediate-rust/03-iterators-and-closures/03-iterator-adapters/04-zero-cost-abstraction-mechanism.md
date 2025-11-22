## Zero Cost Abstraction Mechanism

How do iterator adaptors achieve zero-cost abstraction? What optimizations does the compiler perform?

---

Iterator chains compile to the same efficient code as hand-written loops through several optimizations:

**Compiler optimizations:**

1. **Inlining** - All closures and adaptor methods inline completely
2. **Monomorphization** - Generic code specialized for concrete types
3. **Loop fusion** - Multiple operations merge into single loop
4. **Dead code elimination** - Unused code paths removed

**Example:**
```rust
// High-level code
let sum: i32 = data.iter()
    .filter(|&&x| x % 2 == 0)
    .map(|&x| x * x)
    .sum();

// Compiles to equivalent of:
let mut sum = 0;
for &x in data.iter() {
    if x % 2 == 0 {
        sum += x * x;
    }
}
```

**Result:** Same assembly code, same performance!

**Why it works:**
- No virtual dispatch (generics, not trait objects)
- No heap allocations for the chain itself
- No function call overhead
- LLVM can optimize the fused loop further

Iterator chains give you functional style with imperative performance. The abstraction truly costs nothing.


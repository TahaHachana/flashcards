## Box for Large Data

When should you use `Box` to avoid stack overflow, and what's the performance trade-off?

---

Use `Box` when data is too large for the stack to prevent stack overflow.

**The problem:**
```rust
// ⚠️ Risky - might overflow stack (2-8MB limit)
// let large_array = [0u8; 10_000_000];
```

**The solution:**
```rust
// ✅ Safe - data on heap
let large_array = Box::new([0u8; 10_000_000]);
```

**When to use Box for large data:**
- Arrays or structs larger than ~1MB
- Data that might grow in size
- When unsure about stack limits

**Performance trade-off:**
```rust
// Stack: Fast (~1ms for 1M allocations)
let small = [0; 100];

// Heap: Slower (~50ms for 1M allocations) but safer
let large = Box::new([0; 1_000_000]);
```

**Trade-off:**
- Stack: Fast but limited (2-8MB)
- Heap (via Box): Slower allocation but virtually unlimited

**Rule of thumb:** Data >1MB → use Box


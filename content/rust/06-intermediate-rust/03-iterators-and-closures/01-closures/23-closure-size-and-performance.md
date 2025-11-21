## Closure Size and Performance

What determines the size of a closure? How do closures perform compared to regular functions?

---

**Closure size is determined by captured variables:**

```rust
let x = 5;              // 4 bytes
let y = String::new();  // 24 bytes (on 64-bit)

let small = |z| z + x;  // Size ≈ size of i32 (4 bytes)
let large = |z| y.len() + z; // Size ≈ size of String (24 bytes)
```

A closure's size equals the sum of all captured variables it stores.

**Performance characteristics:**

1. **Zero-cost abstraction** - Non-capturing closures compile to regular functions
2. **Inlining** - Compiler typically inlines closures
3. **No heap allocation** - Unless using `Box<dyn Fn>`
4. **Static dispatch** - When using generic `F: Fn`, no runtime cost

**Cost comparison:**
```rust
// Zero runtime cost (inlined)
numbers.iter().map(|x| x * 2).sum()

// Same as manually written loop
let mut sum = 0;
for x in numbers.iter() {
    sum += x * 2;
}
```

Closures with captured variables have no runtime overhead beyond storing those values.


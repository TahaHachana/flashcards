## Array Bounds Safety

How does Rust prevent buffer overflow vulnerabilities with arrays?

---

Rust checks array bounds at runtime and panics if an index is out of bounds, unlike C/C++ which allows unsafe access.

```rust
let arr = [1, 2, 3];
let x = arr[5];  // ❌ Panics instead of accessing invalid memory
```


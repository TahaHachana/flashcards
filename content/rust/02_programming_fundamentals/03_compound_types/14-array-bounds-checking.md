## Array Bounds Checking

What happens when you access an invalid array index?

---

Rust checks bounds at runtime and panics if the index is out of bounds, preventing buffer overflow vulnerabilities.

```rust
let arr = [1, 2, 3];
let x = arr[10];  // ❌ Panics: index out of bounds
```


## Function Inlining

What is function inlining and how does it optimize code?

---

Inlining inserts small function bodies directly into calling code, eliminating function call overhead. The compiler can further optimize the inlined code.

```rust
fn add(a: i32, b: i32) -> i32 { a + b }
let result = add(3, 4);
// Compiles to: let result = 7;
```


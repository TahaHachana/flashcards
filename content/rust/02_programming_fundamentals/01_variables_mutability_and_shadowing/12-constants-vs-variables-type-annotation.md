## Constants vs Variables Type Annotation

Is type annotation required for constants? What about variables?

---

Type annotation is required for constants. For variables, it's optional (usually inferred).

```rust
const MAX_POINTS: u32 = 100;  // Must annotate
let x = 5;                    // Type inferred
let y: i32 = 5;              // Can annotate
```


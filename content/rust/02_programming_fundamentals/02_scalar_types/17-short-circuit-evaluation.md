## Short-Circuit Evaluation

How do && and || operators use short-circuit evaluation?

---

They stop evaluating as soon as the result is determined. && stops on false, || stops on true.

```rust
let x = false && expensive_function();  // Not called
let y = true || expensive_function();   // Not called
```


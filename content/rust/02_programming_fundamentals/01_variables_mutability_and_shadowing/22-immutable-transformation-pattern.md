## Immutable Transformation Pattern

How does shadowing enable immutable transformations?

---

You can transform values through multiple steps while keeping each step immutable. Each shadow creates a new immutable variable.

```rust
let x = 5;        // Immutable
let x = x + 1;    // New immutable x = 6
let x = x * 2;    // New immutable x = 12
// All values were immutable at each step
```


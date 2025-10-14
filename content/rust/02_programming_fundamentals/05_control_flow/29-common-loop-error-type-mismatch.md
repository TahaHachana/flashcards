## Common Loop Error - Type Mismatch

What's wrong with this if expression?

```rust
let value = if condition { 5 } else { "six" };
```

---

Type mismatch - both branches must return the same type. Fix: use the same type in both branches.

```rust
let value = if condition { 5 } else { 6 };
```


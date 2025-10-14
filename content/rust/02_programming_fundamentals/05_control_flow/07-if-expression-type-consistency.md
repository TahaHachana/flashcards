## if Expression Type Consistency

What requirement must all branches of an if expression meet when used in assignments?

---

All branches must return the same type.

```rust
let x = if condition { 5 } else { "six" };  // ❌ Error
let x = if condition { 5 } else { 6 };      // ✅ OK
```


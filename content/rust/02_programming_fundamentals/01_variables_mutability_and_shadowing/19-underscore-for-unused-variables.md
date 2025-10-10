## Underscore for Unused Variables

How do you suppress warnings for intentionally unused variables?

---

Prefix the variable name with an underscore. This tells the compiler the variable is intentionally unused.

```rust
let _unused = 5;           // No warning
let x = 10;               // Warning if never used
```


## Pattern 7 Higher-Order Functions

How do lifetimes work with higher-order functions that take closures or function pointers?

```rust
fn apply_filter<'a, F>(data: &'a [i32], predicate: F) -> Vec<&'a i32>
where
    F: Fn(&i32) -> bool,
```

---

The lifetime flows from input through closure logic to output. Generic function type parameter `F` represents the closure, and closure borrows match the input lifetime. Mental shortcut: "Closure borrows, doesn't own" → input lifetime flows through. Used when applying user-provided logic to borrowed data.


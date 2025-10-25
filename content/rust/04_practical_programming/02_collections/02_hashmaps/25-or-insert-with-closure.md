## Or Insert With Closure

What's the difference between `.or_insert(value)` and `.or_insert_with(|| value)`?

---

`.or_insert(value)`: Evaluates `value` immediately, even if not needed

`.or_insert_with(|| value)`: Evaluates closure only if key is vacant (lazy evaluation)

Use `.or_insert_with()` when creating the default value is expensive:
```rust
map.entry(key).or_insert_with(|| expensive_computation());
```


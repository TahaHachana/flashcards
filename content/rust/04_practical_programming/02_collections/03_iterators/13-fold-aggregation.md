## Fold Aggregation

What does `.fold()` do and what are its two parameters?

---

`.fold()` combines all items into a single value (reduce/aggregate).

**Parameters**:
1. Initial accumulator value
2. Closure: `|accumulator, item| -> new_accumulator`

```rust
let sum = vec.iter().fold(0, |acc, x| acc + x);
// 0 + 1 + 2 + 3 = 6
```


## Iterator Chain Composition

Show a complex iterator chain combining multiple adapters and a consumer. Explain the execution order.

---

Iterator chains combine multiple operations into a single, efficient pipeline:

**Complex example:**
```rust
let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let result: Vec<String> = numbers
    .iter()                          // 1. Create iterator
    .filter(|&&x| x % 2 == 0)       // 2. Keep evens
    .map(|&x| x * x)                 // 3. Square them
    .take(3)                         // 4. Take first 3
    .enumerate()                     // 5. Add indices
    .map(|(i, x)| format!("#{}: {}", i, x))  // 6. Format
    .collect();                      // 7. Consume into Vec

// ["#0: 4", "#1: 16", "#2: 36"]
```

**Execution order (lazy evaluation):**

Nothing happens until `.collect()` is called. Then:

1. `.iter()` produces &1
2. `.filter()` checks 1 % 2 == 0 → false, skips
3. `.iter()` produces &2
4. `.filter()` checks 2 % 2 == 0 → true, passes
5. `.map()` squares to 4
6. `.take()` counts (1 of 3), passes
7. `.enumerate()` adds index (0, 4)
8. `.map()` formats "#0: 4"
9. `.collect()` stores in Vec
10. Repeat for 4, 6...
11. After 3 items, `.take()` stops entire chain

**Key insight:** Operations are performed element-by-element, not stage-by-stage. Each element flows through the entire pipeline before the next element starts.

**Visual flow:**
```
1 → filter(❌) → stop
2 → filter(✓) → map(4) → take(✓) → enumerate(0,4) → format → collect
4 → filter(✓) → map(16) → take(✓) → enumerate(1,16) → format → collect
6 → filter(✓) → map(36) → take(✓) → enumerate(2,36) → format → collect
8 → take(❌) → chain stops
```


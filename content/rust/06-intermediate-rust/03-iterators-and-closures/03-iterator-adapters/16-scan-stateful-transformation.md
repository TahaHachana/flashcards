## Scan Stateful Transformation

How does `.scan()` differ from `.fold()`? Show a running sum example.

---

`.scan()` is like `.fold()` but emits intermediate values instead of just the final result.

**Key difference:**
- `.fold()` - Returns single final value
- `.scan()` - Returns iterator of intermediate values

**Signature:**
```rust
fn scan<St, B, F>(self, initial_state: St, f: F) -> Scan<Self, St, F>
where
    F: FnMut(&mut St, Self::Item) -> Option<B>
```

**Running sum:**
```rust
let running_sums: Vec<i32> = vec![1, 2, 3, 4, 5]
    .into_iter()
    .scan(0, |acc, x| {
        *acc += x;
        Some(*acc)  // Emit current accumulator
    })
    .collect();
// [1, 3, 6, 10, 15]

// Compare with fold:
let final_sum = vec![1, 2, 3, 4, 5].iter().fold(0, |acc, &x| acc + x);
// 15 (just final value)
```

**Running average:**
```rust
let running_avgs: Vec<f64> = numbers.iter()
    .scan((0.0, 0), |(sum, count), &x| {
        *sum += x as f64;
        *count += 1;
        Some(*sum / *count as f64)
    })
    .collect();
```

**Computing differences (with previous element):**
```rust
let differences: Vec<i32> = numbers.iter()
    .scan(None, |prev, &x| {
        let result = prev.map(|p| x - p);
        *prev = Some(x);
        Some(result)
    })
    .filter_map(|x| x)  // Remove first None
    .collect();
```

**Early termination:**
```rust
// Stop when budget exceeded
let within_budget: Vec<Item> = items.iter()
    .scan(0, |budget, item| {
        if *budget + item.cost <= MAX_BUDGET {
            *budget += item.cost;
            Some(item.clone())
        } else {
            None  // Returning None stops iteration
        }
    })
    .collect();
```

Use `.scan()` when you need intermediate accumulator values, not just the final result.


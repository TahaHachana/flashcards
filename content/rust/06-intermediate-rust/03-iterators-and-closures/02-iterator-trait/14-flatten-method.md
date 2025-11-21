## Flatten Method

What does `.flatten()` do? Show examples with nested structures and Options.

---

`.flatten()` flattens nested iterators or `Option`/`Result` values into a single-level iterator.

**Flattening nested vectors:**
```rust
let nested = vec![vec![1, 2], vec![3, 4, 5], vec![6]];

let flat: Vec<i32> = nested.iter()
    .flatten()
    .copied()
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Flattening Options (removes None):**
```rust
let options = vec![Some(1), None, Some(2), None, Some(3)];

let values: Vec<i32> = options.into_iter()
    .flatten()
    .collect();
// [1, 2, 3]
```

**Flattening Results (keeps Ok, discards Err):**
```rust
let results = vec![Ok(1), Err("error"), Ok(2), Ok(3)];

let successes: Vec<i32> = results.into_iter()
    .flatten()
    .collect();
// [1, 2, 3]
```

**Combined with map (common pattern):**
```rust
let numbers = vec!["1", "not a number", "2", "3"];

let parsed: Vec<i32> = numbers.iter()
    .map(|s| s.parse::<i32>())  // Returns Result
    .flatten()                   // Keep only Ok values
    .collect();
// [1, 2, 3]
```

`.flatten()` is especially useful for filtering out None/Err values in iterator chains.


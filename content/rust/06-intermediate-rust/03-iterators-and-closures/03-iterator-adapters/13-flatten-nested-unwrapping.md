## Flatten Nested Unwrapping

What does `.flatten()` do with different types? Show examples with nested vectors, Options, and Results.

---

`.flatten()` removes one level of nesting from nested iterators or Option/Result values.

**Flattening nested vectors:**
```rust
let nested = vec![vec![1, 2], vec![3, 4, 5], vec![6]];

let flat: Vec<i32> = nested.into_iter()
    .flatten()
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Flattening Options (removes None):**
```rust
let options = vec![Some(1), None, Some(2), None, Some(3)];

let values: Vec<i32> = options.into_iter()
    .flatten()
    .collect();
// [1, 2, 3] - None values disappear
```

**Flattening Results (keeps Ok, discards Err):**
```rust
let results = vec![Ok(1), Err("error"), Ok(2), Ok(3)];

let successes: Vec<i32> = results.into_iter()
    .flatten()
    .collect();
// [1, 2, 3] - Err values filtered out
```

**With map (common pattern):**
```rust
let parsed: Vec<i32> = vec!["1", "not a number", "2", "3"]
    .iter()
    .map(|s| s.parse::<i32>())  // Returns Result
    .flatten()  // Keeps Ok, discards Err
    .collect();
// [1, 2, 3]
```

**Splitting strings:**
```rust
let words: Vec<&str> = sentences.iter()
    .map(|s| s.split_whitespace())  // Returns iterator
    .flatten()
    .collect();
```

**Equivalent to flat_map:**
```rust
iter.map(f).flatten()
// Same as:
iter.flat_map(f)
```

Only removes ONE level of nesting. For deeply nested structures, need multiple `.flatten()` calls or recursive approach.


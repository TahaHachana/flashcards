## Collect with Result and Option

How does `.collect()` behave with iterators of `Result` or `Option`? Show both success and failure cases.

---

`.collect()` has special behavior for Result and Option - it "flips" the container and iterator.

**With Result - stops at first error:**

**Success:**
```rust
let results: Result<Vec<i32>, _> = 
    vec!["1", "2", "3"]
        .iter()
        .map(|s| s.parse::<i32>())
        .collect();
// Ok([1, 2, 3])
```

**Failure:**
```rust
let results: Result<Vec<i32>, _> = 
    vec!["1", "not a number", "3"]
        .iter()
        .map(|s| s.parse::<i32>())
        .collect();
// Err(ParseIntError) - stops immediately at error
```

**With Option - None if any is None:**

**All Some:**
```rust
let all: Option<Vec<i32>> = 
    vec![Some(1), Some(2), Some(3)]
        .into_iter()
        .collect();
// Some([1, 2, 3])
```

**Has None:**
```rust
let has_none: Option<Vec<i32>> = 
    vec![Some(1), None, Some(3)]
        .into_iter()
        .collect();
// None - one None makes entire result None
```

**Key behavior:** Transforms `Iterator<Item = Result<T, E>>` into `Result<Vec<T>, E>` and `Iterator<Item = Option<T>>` into `Option<Vec<T>>`.

This is extremely useful for error propagation in pipelines.


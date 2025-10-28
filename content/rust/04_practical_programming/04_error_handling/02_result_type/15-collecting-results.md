## Collecting Results

How do you collect an iterator of Results into a Result of a collection?

---

Use `.collect()` which stops at the first error:

```rust
let strings = vec!["1", "2", "3"];
let numbers: Result<Vec<i32>, _> = strings
    .iter()
    .map(|s| s.parse::<i32>())
    .collect();
// Ok([1, 2, 3])

let bad = vec!["1", "bad", "3"];
let result: Result<Vec<i32>, _> = bad
    .iter()
    .map(|s| s.parse::<i32>())
    .collect();
// Err(...) - stops at first error
```

If any element is `Err`, the entire collection becomes that `Err`.


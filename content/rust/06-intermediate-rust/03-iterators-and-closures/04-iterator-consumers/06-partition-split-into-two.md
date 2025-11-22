## Partition Split Into Two

What does `.partition()` do? When would you use it instead of `.filter()`?

---

`.partition()` splits an iterator into two collections based on a predicate - elements that match and elements that don't.

**Signature:**
```rust
fn partition<B, F>(self, f: F) -> (B, B)
where
    F: FnMut(&Self::Item) -> bool
```

**Basic usage:**
```rust
let numbers = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let (evens, odds): (Vec<_>, Vec<_>) = numbers.into_iter()
    .partition(|&n| n % 2 == 0);
// evens: [2, 4, 6, 8, 10]
// odds: [1, 3, 5, 7, 9]
```

**Separating valid/invalid:**
```rust
let (valid, invalid): (Vec<_>, Vec<_>) = data.into_iter()
    .partition(|item| item.is_valid());
```

**With Results:**
```rust
let results = vec![Ok(1), Err("e1"), Ok(2), Err("e2")];
let (successes, failures): (Vec<_>, Vec<_>) = results.into_iter()
    .partition(|r| r.is_ok());
```

**When to use:**
- Need BOTH filtered and non-filtered elements
- Processing two separate groups differently
- Error handling where you need both successes and failures

**Compared to filter:**
```rust
// filter - only get one side
let evens: Vec<_> = nums.iter().filter(|&&x| x % 2 == 0).collect();

// partition - get both sides
let (evens, odds) = nums.into_iter().partition(|&x| x % 2 == 0);
```


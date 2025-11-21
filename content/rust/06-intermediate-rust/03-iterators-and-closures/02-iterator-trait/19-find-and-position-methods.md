## Find and Position Methods

What do `.find()` and `.position()` methods do? How do they differ?

---

Both search for the first element matching a condition, but return different information.

**`.find()` - Returns the element itself:**
```rust
let numbers = vec![1, 3, 5, 6, 8, 9];

let first_even = numbers.iter()
    .find(|&&x| x % 2 == 0);
// Some(&6) - returns reference to the element
```

**`.position()` - Returns the index:**
```rust
let position = numbers.iter()
    .position(|&x| x % 2 == 0);
// Some(3) - index where 6 is located
```

**Key differences:**

| Method | Returns | Use when |
|--------|---------|----------|
| `.find()` | `Option<Item>` | You need the value |
| `.position()` | `Option<usize>` | You need the index |

**Both short-circuit (stop early):**
```rust
let first_big = (0..)  // Infinite iterator
    .find(|&x| x > 1000);
// Some(1001) - stops as soon as found
```

**Common patterns:**
```rust
// Find then use value
if let Some(item) = vec.iter().find(|x| condition(x)) {
    process(item);
}

// Find then access original
if let Some(pos) = vec.iter().position(|x| condition(x)) {
    let item = &vec[pos];
}
```

Both consume the iterator up to the found element (or completely if not found).


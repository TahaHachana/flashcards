## Take and Skip Methods

What do `.take()` and `.skip()` methods do? Show how they work together.

---

`.take(n)` takes the first n elements, `.skip(n)` skips the first n elements.

**`.take()` - Take first N:**
```rust
let numbers = vec![1, 2, 3, 4, 5];

let first_three: Vec<i32> = numbers.iter()
    .copied()
    .take(3)
    .collect();
// [1, 2, 3]
```

**`.skip()` - Skip first N:**
```rust
let after_two: Vec<i32> = numbers.iter()
    .copied()
    .skip(2)
    .collect();
// [3, 4, 5]
```

**Combined usage:**
```rust
let data = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

let middle: Vec<i32> = data.iter()
    .skip(3)    // Skip first 3: [3, 4, 5, 6, 7, 8, 9]
    .take(4)    // Take next 4: [3, 4, 5, 6]
    .copied()
    .collect();
// [3, 4, 5, 6]
```

**Useful with infinite iterators:**
```rust
let first_ten_evens: Vec<i32> = (0..)  // Infinite
    .filter(|x| x % 2 == 0)
    .take(10)  // Limit to 10 items
    .collect();
// [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```


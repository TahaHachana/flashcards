## Sum and Product Methods

What do `.sum()` and `.product()` methods do? What trait requirement do they have?

---

`.sum()` and `.product()` are convenient consumers for arithmetic operations on numeric iterators.

**`.sum()` - Add all elements:**
```rust
let total: i32 = vec![1, 2, 3, 4, 5].iter().sum();
// 15

let float_sum: f64 = vec![1.5, 2.5, 3.0].iter().sum();
// 7.0
```

**`.product()` - Multiply all elements:**
```rust
let factorial: i32 = (1..=5).product();
// 120 (5! = 5 × 4 × 3 × 2 × 1)

let result: f64 = vec![2.0, 3.0, 4.0].iter().product();
// 24.0
```

**Type annotation required:**
```rust
// Need to specify output type
let sum: i32 = iter.sum();  // Which numeric type?
```

**Trait requirement:**
Elements must implement `Sum` or `Product` trait (all standard numeric types do).

**Common with filtered/mapped data:**
```rust
let even_sum: i32 = (1..=10)
    .filter(|x| x % 2 == 0)
    .sum();
// 30 (2 + 4 + 6 + 8 + 10)

let squared_product: i32 = vec![2, 3, 4].iter()
    .map(|x| x * x)
    .product();
// 576 (4 × 9 × 16)
```

These are specialized versions of `.fold()` for common arithmetic operations.


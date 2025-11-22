## Sum and Product Arithmetic

What do `.sum()` and `.product()` do? What trait requirement do they have?

---

`.sum()` adds all elements; `.product()` multiplies all elements.

**Signatures:**
```rust
fn sum<S>(self) -> S where S: Sum<Self::Item>
fn product<P>(self) -> P where P: Product<Self::Item>
```

**Basic examples:**
```rust
// Sum
let total: i32 = vec![1, 2, 3, 4, 5].iter().sum();
// 15

// Product
let factorial: i32 = (1..=5).product();
// 120 (5! = 5 × 4 × 3 × 2 × 1)
```

**With filtering:**
```rust
let even_sum: i32 = (1..=10)
    .filter(|x| x % 2 == 0)
    .sum();
// 30 (2 + 4 + 6 + 8 + 10)
```

**With mapping:**
```rust
let sum_of_squares: i32 = vec![1, 2, 3, 4, 5]
    .iter()
    .map(|x| x * x)
    .sum();
// 55 (1 + 4 + 9 + 16 + 25)
```

**Type annotation required:**
```rust
let total: i32 = iter.sum();  // Must specify type
// or
let total = iter.sum::<i32>();
```

**Trait requirement:** Types must implement `Sum` or `Product` trait (all standard numeric types do: i32, f64, etc.).

These are specialized versions of fold for common arithmetic operations.


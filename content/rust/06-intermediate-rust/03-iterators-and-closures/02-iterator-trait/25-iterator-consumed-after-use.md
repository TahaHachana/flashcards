## Iterator Consumed After Use

What's wrong with this code and why?

```rust
let iter = vec![1, 2, 3].into_iter();
let sum: i32 = iter.sum();
let product: i32 = iter.product();
```

---

**Problem:** Iterator is consumed (moved) by the first consumer method, so it can't be used again.

```rust
let iter = vec![1, 2, 3].into_iter();
let sum: i32 = iter.sum();  // Consumes iter
// let product: i32 = iter.product(); // ERROR: iter was moved
```

**Error message:**
```
error[E0382]: use of moved value: `iter`
  |
  | let sum: i32 = iter.sum();  // iter moved here
  | let product: i32 = iter.product(); // value used after move
```

**Fix 1: Create separate iterators:**
```rust
let vec = vec![1, 2, 3];
let sum: i32 = vec.iter().sum();
let product: i32 = vec.iter().product();
```

**Fix 2: Clone the collection:**
```rust
let iter1 = vec.clone().into_iter();
let iter2 = vec.into_iter();
let sum = iter1.sum();
let product = iter2.product();
```

**Fix 3: Use a single pass with fold:**
```rust
let (sum, product) = vec.iter()
    .fold((0, 1), |(sum, prod), &x| (sum + x, prod * x));
```

**Key rule:** Consuming methods (`.sum()`, `.collect()`, `.fold()`, etc.) take ownership of `self`, so the iterator is moved and unavailable afterward.


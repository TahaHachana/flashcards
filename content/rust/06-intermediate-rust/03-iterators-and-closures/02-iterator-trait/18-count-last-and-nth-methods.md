## Count Last and Nth Methods

What do `.count()`, `.last()`, and `.nth()` methods do? What's important to know about `.nth()`?

---

All three are consuming methods that traverse the iterator.

**`.count()` - Count elements:**
```rust
let count = vec![1, 2, 3, 4, 5].iter().count();
// 5

let even_count = (1..=10)
    .filter(|x| x % 2 == 0)
    .count();
// 5
```

**`.last()` - Get last element (consumes entire iterator):**
```rust
let last = vec![1, 2, 3, 4, 5].iter().last();
// Some(&5)

let last_even = (1..=10)
    .filter(|x| x % 2 == 0)
    .last();
// Some(10)
```

**`.nth(n)` - Get nth element (zero-indexed):**
```rust
let mut iter = vec![10, 20, 30, 40, 50].into_iter();

let third = iter.nth(2);  // Some(30) - gets index 2
let next = iter.nth(0);   // Some(40) - next element
// NOT iter.nth(3) - that would skip 40
```

**IMPORTANT about `.nth()`:**
- Consumes elements up to and including index n
- Index is relative to current position, not original start
- Can't go backwards

```rust
let mut iter = (0..10);
iter.nth(5);  // Consumes 0,1,2,3,4,5 returns 5
iter.nth(0);  // Returns 6 (next element)
iter.nth(2);  // Skips 7,8, returns 9
```

All three methods consume the iterator completely or partially.


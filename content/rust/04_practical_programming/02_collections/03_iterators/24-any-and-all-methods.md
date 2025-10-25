## Any and All Methods

What do `.any()` and `.all()` do?

---

Both take a predicate and return `bool`:

`.any()`: True if **at least one** item matches
```rust
let has_even = vec![1, 3, 4].iter().any(|&x| x % 2 == 0);
// true (4 is even)
```

`.all()`: True if **all** items match
```rust
let all_positive = vec![1, 2, 3].iter().all(|&x| x > 0);
// true
```


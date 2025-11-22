## Find First Match

What does `.find()` do? How does it perform on large iterators and infinite iterators?

---

`.find()` returns the first element matching a predicate, short-circuiting on match.

**Signature:**
```rust
fn find<P>(self, predicate: P) -> Option<Self::Item>
where P: FnMut(&Self::Item) -> bool
```

**Basic usage:**
```rust
let numbers = vec![1, 3, 5, 6, 7, 9];

let first_even = numbers.iter()
    .find(|&&x| x % 2 == 0);
// Some(&6)

let first_big = numbers.iter()
    .find(|&&x| x > 100);
// None
```

**Short-circuits - critical for performance:**
```rust
// Only checks until match found
let found = (0..1_000_000)
    .find(|&x| x == 500);
// Some(500) - stops immediately, doesn't check 999,500 remaining
```

**Works with infinite iterators:**
```rust
let first_big = (0..)  // Infinite iterator
    .find(|&x| x > 1000);
// Some(1001) - stops and returns, doesn't hang
```

**With complex predicates:**
```rust
let user = users.iter()
    .find(|u| u.email == target && u.is_active);
```

**Returns element, not index:**
```rust
// find returns the element
let element: Option<&i32> = numbers.iter().find(predicate);

// Use position() for index
let index: Option<usize> = numbers.iter().position(predicate);
```

Performance: O(n) worst case, but short-circuits mean average case is often much better.


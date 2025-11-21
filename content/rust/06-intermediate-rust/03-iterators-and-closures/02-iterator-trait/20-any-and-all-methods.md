## Any and All Methods

What do `.any()` and `.all()` methods do? Do they always check every element?

---

`.any()` and `.all()` test whether elements match a predicate, returning a boolean.

**`.any()` - True if ANY element matches:**
```rust
let numbers = vec![1, 3, 5, 6, 9];

let has_even = numbers.iter()
    .any(|&x| x % 2 == 0);
// true (6 is even)

let has_negative = numbers.iter()
    .any(|&x| x < 0);
// false
```

**`.all()` - True if ALL elements match:**
```rust
let all_positive = numbers.iter()
    .all(|&x| x > 0);
// true

let all_even = numbers.iter()
    .all(|&x| x % 2 == 0);
// false (1, 3, 5, 9 are odd)
```

**Both short-circuit (don't check everything):**

`.any()` stops at first `true`:
```rust
vec![1, 3, 5, 6, 8].iter()
    .any(|&x| x % 2 == 0)
// Stops at 6, doesn't check 8
```

`.all()` stops at first `false`:
```rust
vec![2, 4, 5, 6, 8].iter()
    .all(|&x| x % 2 == 0)
// Stops at 5, doesn't check 6 or 8
```

**Negation relationship:**
```rust
!vec.iter().any(|x| condition(x))
// Equivalent to:
vec.iter().all(|x| !condition(x))
```

**Usage:** Checking properties of collections without manual loops.


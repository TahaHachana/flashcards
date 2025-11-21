## Cycle and Rev Methods

What do `.cycle()` and `.rev()` methods do? What are their requirements and typical uses?

---

**`.cycle()` - Repeats iterator infinitely:**
```rust
let pattern = vec![1, 2, 3].iter().cycle();

let repeated: Vec<i32> = pattern
    .take(7)
    .copied()
    .collect();
// [1, 2, 3, 1, 2, 3, 1]
```

**Common with `.zip()`:**
```rust
let labels = ["even", "odd"].iter().cycle();
let numbers = (0..6);

for (num, label) in numbers.zip(labels) {
    println!("{}: {}", num, label);
}
// 0: even, 1: odd, 2: even, 3: odd, 4: even, 5: odd
```

**⚠️ Warning:** `.cycle()` creates infinite iterator - MUST use `.take()` or similar to limit.

**`.rev()` - Reverses iterator:**
```rust
let reversed: Vec<i32> = vec![1, 2, 3, 4, 5].iter()
    .rev()
    .copied()
    .collect();
// [5, 4, 3, 2, 1]
```

**Requirement:** Iterator must implement `DoubleEndedIterator` (has `.next_back()`):
```rust
// Works - Vec implements DoubleEndedIterator
vec.iter().rev()

// Doesn't work - .filter() doesn't know size
vec.iter().filter(|x| condition(x)).rev()  // ERROR
```

**Common pattern - search from end:**
```rust
let last_even_position = (0..10)
    .rev()  // Search backwards
    .position(|x| x % 2 == 0);
```

`.rev()` is zero-cost - just changes iteration direction.


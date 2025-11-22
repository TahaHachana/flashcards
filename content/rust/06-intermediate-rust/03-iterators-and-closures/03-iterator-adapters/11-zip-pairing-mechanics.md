## Zip Pairing Mechanics

How does `.zip()` work? What happens when iterators have different lengths?

---

`.zip()` combines two iterators element-wise into pairs (tuples).

**Basic usage:**
```rust
let names = vec!["Alice", "Bob", "Carol"];
let ages = vec![30, 25, 35];

let pairs: Vec<_> = names.iter()
    .zip(ages.iter())
    .collect();
// [("Alice", 30), ("Bob", 25), ("Carol", 35)]
```

**Creating HashMap:**
```rust
let map: HashMap<_, _> = keys.into_iter()
    .zip(values.into_iter())
    .collect();
```

**Length handling - stops at shortest:**
```rust
let short = vec![1, 2, 3];
let long = vec![10, 20, 30, 40, 50];

let zipped: Vec<_> = short.iter()
    .zip(long.iter())
    .collect();
// [(1, 10), (2, 20), (3, 30)]
// Stops when short is exhausted
```

**Zipping three iterators:**
```rust
let triples = names.iter()
    .zip(ages.iter())
    .zip(cities.iter())
    .map(|((name, age), city)| (name, age, city))
    .collect();
```

**With infinite iterator:**
```rust
let labeled: Vec<_> = (1..)  // Infinite numbers
    .zip(items.iter())  // Finite items
    .map(|(num, item)| format!("{}. {}", num, item))
    .collect();
// Stops when items exhausted
```

**Computing differences:**
```rust
let diffs: Vec<i32> = numbers[1..].iter()
    .zip(numbers[..numbers.len()-1].iter())
    .map(|(next, prev)| next - prev)
    .collect();
```

Always stops at the shorter iterator - no panic, no padding.


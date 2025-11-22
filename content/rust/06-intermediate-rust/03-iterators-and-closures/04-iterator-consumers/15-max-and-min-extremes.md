## Max and Min Extremes

What do `.max()` and `.min()` do? What trait requirement do they have, and how do you handle floats?

---

`.max()` and `.min()` find the maximum or minimum element.

**Signatures:**
```rust
fn max(self) -> Option<Self::Item>
where Self::Item: Ord

fn min(self) -> Option<Self::Item>
where Self::Item: Ord
```

**Basic usage:**
```rust
let numbers = vec![3, 7, 2, 9, 1];

let max = numbers.iter().max();
// Some(&9)

let min = numbers.iter().min();
// Some(&1)
```

**Trait requirement: `Ord` (total ordering)**
- Works: integers, strings, chars
- Doesn't work: floats (no Ord due to NaN)

**Handling floats - use fold:**
```rust
let floats = vec![3.5, 7.2, 2.1, 9.8, 1.4];

// Can't use .max() directly on floats
// let max = floats.iter().max();  // ERROR: no Ord

// Use fold instead
let max = floats.iter()
    .fold(f64::NEG_INFINITY, |a, &b| a.max(b));
// 9.8

let min = floats.iter()
    .fold(f64::INFINITY, |a, &b| a.min(b));
// 1.4
```

**Custom comparison with max_by_key:**
```rust
let people = vec![
    Person { name: "Alice", age: 30 },
    Person { name: "Bob", age: 25 },
    Person { name: "Carol", age: 35 },
];

let oldest = people.iter().max_by_key(|p| p.age);
// Some(&Person { name: "Carol", age: 35 })

let longest_name = people.iter().max_by_key(|p| p.name.len());
```

**Empty iterator:**
```rust
Vec::<i32>::new().iter().max()  // None
```

Performance: O(n) - must check every element.


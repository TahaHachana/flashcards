## Zip Method

What does `.zip()` do? How does it handle iterators of different lengths?

---

`.zip()` combines two iterators into a single iterator of pairs/tuples.

**Basic usage:**
```rust
let names = vec!["Alice", "Bob", "Carol"];
let ages = vec![30, 25, 35];

for (name, age) in names.iter().zip(ages.iter()) {
    println!("{} is {} years old", name, age);
}
// Alice is 30 years old
// Bob is 25 years old
// Carol is 35 years old
```

**Collecting zipped data:**
```rust
let pairs: Vec<(&str, i32)> = names.iter()
    .zip(ages.iter())
    .map(|(&n, &a)| (n, a))
    .collect();
// [("Alice", 30), ("Bob", 25), ("Carol", 35)]
```

**Different lengths - stops at shortest:**
```rust
let a = vec![1, 2, 3, 4, 5];
let b = vec!["a", "b", "c"];  // Shorter

let zipped: Vec<_> = a.iter().zip(b.iter()).collect();
// [(1, "a"), (2, "b"), (3, "c")]
// Stops when b is exhausted
```

**Multiple zips:**
```rust
let triples = a.iter()
    .zip(b.iter())
    .zip(c.iter())
    .map(|((x, y), z)| (*x, *y, *z));
```

**Key rule:** Iteration stops when the shortest iterator is exhausted.


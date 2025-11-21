## Fold Method

What does `.fold()` do? Explain its parameters and show examples beyond simple summation.

---

`.fold()` reduces an iterator to a single value by repeatedly applying a function with an accumulator.

**Signature:**
```rust
fn fold<B, F>(self, init: B, f: F) -> B
where
    F: FnMut(B, Self::Item) -> B
```

**Parameters:**
- `init` - Initial accumulator value
- `f` - Closure taking (accumulator, next_item) → new accumulator

**Simple sum:**
```rust
let sum = vec![1, 2, 3, 4, 5].iter()
    .fold(0, |acc, &x| acc + x);
// 15
```

**Building a string:**
```rust
let sentence = vec!["Hello", "world", "from", "Rust"].iter()
    .fold(String::new(), |mut acc, &word| {
        if !acc.is_empty() {
            acc.push(' ');
        }
        acc.push_str(word);
        acc
    });
// "Hello world from Rust"
```

**Aggregating into struct:**
```rust
#[derive(Debug)]
struct Stats {
    count: u32,
    sum: i32,
}

let stats = vec![1, 2, 3, 4, 5].iter()
    .fold(Stats { count: 0, sum: 0 }, |mut acc, &x| {
        acc.count += 1;
        acc.sum += x;
        acc
    });
// Stats { count: 5, sum: 15 }
```

`.fold()` is powerful for complex reductions beyond simple arithmetic.


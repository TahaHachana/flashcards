## Fold Universal Reducer

What does `.fold()` do? Show examples beyond simple summation, including building complex structures.

---

`.fold()` reduces an iterator to a single value using an accumulator pattern.

**Signature:**
```rust
fn fold<B, F>(self, init: B, f: F) -> B
where
    F: FnMut(B, Self::Item) -> B
```

**Parameters:**
- `init` - Initial accumulator value
- `f` - Closure: (accumulator, next_item) → new_accumulator

**Simple sum:**
```rust
let sum = vec![1, 2, 3, 4, 5].iter()
    .fold(0, |acc, &x| acc + x);
// 15
```

**Building strings:**
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

**Building complex structure:**
```rust
#[derive(Debug)]
struct Stats {
    count: usize,
    sum: i32,
    min: i32,
    max: i32,
}

let stats = numbers.iter().fold(
    Stats {
        count: 0,
        sum: 0,
        min: i32::MAX,
        max: i32::MIN,
    },
    |mut acc, &x| {
        acc.count += 1;
        acc.sum += x;
        acc.min = acc.min.min(x);
        acc.max = acc.max.max(x);
        acc
    }
);
```

**Grouping elements:**
```rust
let groups: HashMap<char, Vec<String>> = words.into_iter()
    .fold(HashMap::new(), |mut map, word| {
        let first = word.chars().next().unwrap();
        map.entry(first)
            .or_insert_with(Vec::new)
            .push(word);
        map
    });
```

**Reversing:**
```rust
let reversed: Vec<i32> = vec![1, 2, 3, 4, 5]
    .into_iter()
    .fold(Vec::new(), |mut acc, x| {
        acc.insert(0, x);  // Insert at front
        acc
    });
// [5, 4, 3, 2, 1]
```

Fold is the most general reduction - any consuming operation can be expressed as fold.


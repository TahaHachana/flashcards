## Fold Universal Reducer

Why is `.fold()` called the "universal reducer"? Show an example beyond simple summation.

---

`.fold()` can express any reduction operation - it's the most general consumer.

**Signature:**
```rust
fn fold<B, F>(self, init: B, f: F) -> B
where F: FnMut(B, Self::Item) -> B
```

**Parameters:**
- `init` - Initial accumulator value
- `f` - Closure: (accumulator, next_item) → new_accumulator

**Beyond summation - building statistics:**
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

let average = stats.sum / stats.count as i32;
```

**Grouping elements:**
```rust
let grouped: HashMap<char, Vec<String>> = words.into_iter()
    .fold(HashMap::new(), |mut map, word| {
        let first_char = word.chars().next().unwrap();
        map.entry(first_char)
            .or_insert_with(Vec::new)
            .push(word);
        map
    });
```

**Why "universal":** Any consuming operation can be expressed as fold - sum, product, collect, max, min, etc. are all specialized folds.


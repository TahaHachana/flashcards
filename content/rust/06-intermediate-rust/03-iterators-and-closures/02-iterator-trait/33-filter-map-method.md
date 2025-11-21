## Filter Map Method

What does `.filter_map()` do? How does it combine filtering and mapping?

---

`.filter_map()` simultaneously filters and transforms elements by taking a closure that returns `Option<T>`.

**How it works:**
- Closure returns `Some(value)` → value is kept and extracted
- Closure returns `None` → element is filtered out

**Signature:**
```rust
fn filter_map<B, F>(self, f: F) -> FilterMap<Self, F>
where
    F: FnMut(Self::Item) -> Option<B>
```

**Example - parsing numbers:**
```rust
let strings = vec!["1", "two", "3", "four", "5"];

let numbers: Vec<i32> = strings.iter()
    .filter_map(|s| s.parse::<i32>().ok())
    .collect();
// [1, 3, 5] - invalid parses are None, filtered out
```

**Compared to separate filter + map:**
```rust
// Less efficient - two passes
strings.iter()
    .filter(|s| s.parse::<i32>().is_ok())
    .map(|s| s.parse::<i32>().unwrap())
    .collect()

// More efficient - single pass
strings.iter()
    .filter_map(|s| s.parse::<i32>().ok())
    .collect()
```

**Working with Option:**
```rust
let options = vec![Some(1), None, Some(2), None, Some(3)];

let values: Vec<i32> = options.iter()
    .filter_map(|&x| x)  // Unwraps Some, filters None
    .collect();
// [1, 2, 3]
```

**Custom transformation:**
```rust
struct Person { name: String, age: Option<u32> }

let adults: Vec<String> = people.iter()
    .filter_map(|p| {
        p.age.and_then(|age| {
            if age >= 18 {
                Some(p.name.clone())
            } else {
                None
            }
        })
    })
    .collect();
```

`.filter_map()` is more efficient than `.filter().map()` and handles Option/Result elegantly.


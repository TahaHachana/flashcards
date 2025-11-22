## Flat Map Combined Operation

What does `.flat_map()` do? Show an example where each element expands into multiple elements.

---

`.flat_map()` maps each element to an iterator, then flattens - combining `.map()` and `.flatten()`.

**Signature:**
```rust
fn flat_map<U, F>(self, f: F) -> FlatMap<Self, U, F>
where
    F: FnMut(Self::Item) -> U,
    U: IntoIterator
```

**Expanding elements:**
```rust
let expanded: Vec<i32> = vec![1, 2, 3]
    .into_iter()
    .flat_map(|x| vec![x, x * 10])
    .collect();
// [1, 10, 2, 20, 3, 30]
// Each element becomes two elements
```

**Splitting text:**
```rust
let words: Vec<&str> = vec!["hello world", "rust programming"]
    .iter()
    .flat_map(|sentence| sentence.split_whitespace())
    .collect();
// ["hello", "world", "rust", "programming"]
```

**Cartesian product-like operation:**
```rust
let pairs: Vec<(i32, char)> = vec![1, 2, 3]
    .into_iter()
    .flat_map(|num| {
        vec!['a', 'b'].into_iter()
            .map(move |ch| (num, ch))
    })
    .collect();
// [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

**Conditional expansion:**
```rust
let result: Vec<Item> = items.iter()
    .flat_map(|item| {
        if item.is_valid() {
            item.get_all_versions()  // Returns Vec
        } else {
            vec![]  // Returns empty Vec
        }
    })
    .collect();
```

**Equivalence:**
```rust
// These are identical:
data.iter().map(f).flatten()
data.iter().flat_map(f)

// flat_map is just syntactic sugar
```

Use when each input element produces zero or more output elements.


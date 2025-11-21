## Enumerate Method

What does `.enumerate()` do? Show its typical usage patterns.

---

`.enumerate()` adds indices to iterator elements, producing `(index, item)` tuples.

**Basic usage:**
```rust
let words = vec!["first", "second", "third"];

for (index, word) in words.iter().enumerate() {
    println!("{}: {}", index, word);
}
// 0: first
// 1: second
// 2: third
```

**Finding position:**
```rust
let numbers = vec![10, 20, 30, 40, 50];

let position = numbers.iter()
    .enumerate()
    .find(|(_, &value)| value == 30)
    .map(|(index, _)| index);
// Some(2)
```

**Creating indexed collection:**
```rust
let indexed: Vec<(usize, i32)> = vec![100, 200, 300]
    .iter()
    .enumerate()
    .map(|(i, &v)| (i, v))
    .collect();
// [(0, 100), (1, 200), (2, 300)]
```

**Building HashMap from indices:**
```rust
let map: HashMap<usize, &str> = words.iter()
    .enumerate()
    .map(|(i, &word)| (i, word))
    .collect();
```

Indices are zero-based and of type `usize`.


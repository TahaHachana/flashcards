## Enumerate Index Addition

What does `.enumerate()` do? Show three practical use cases.

---

`.enumerate()` adds zero-based indices, transforming `Item` into `(usize, Item)` tuples.

**Basic usage:**
```rust
for (i, value) in vec!["a", "b", "c"].iter().enumerate() {
    println!("{}: {}", i, value);
}
// 0: a
// 1: b
// 2: c
```

**Use case 1: Finding index of element**
```rust
let position = data.iter()
    .enumerate()
    .find(|(_, &val)| val == target)
    .map(|(idx, _)| idx);
// Returns Option<usize> with index
```

**Use case 2: Filtering by index**
```rust
// Every third element
let every_third: Vec<i32> = numbers.iter()
    .enumerate()
    .filter(|(i, _)| i % 3 == 0)
    .map(|(_, &val)| val)
    .collect();
```

**Use case 3: Line numbering**
```rust
let numbered: Vec<String> = lines.iter()
    .enumerate()
    .map(|(i, line)| format!("{:3}: {}", i + 1, line))
    .collect();
// "  1: first line"
// "  2: second line"
```

**Pattern - processing with previous element:**
```rust
let diffs: Vec<i32> = numbers.iter()
    .enumerate()
    .map(|(i, &val)| {
        if i == 0 { 0 }
        else { val - numbers[i - 1] }
    })
    .collect();
```

Indices are `usize` and zero-based. Can offset by mapping: `(i + 1, item)` for 1-based.


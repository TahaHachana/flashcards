## Chain Method

What does `.chain()` do? Show how to concatenate multiple iterators.

---

`.chain()` concatenates two iterators, creating a single iterator that yields elements from both in sequence.

**Basic usage:**
```rust
let a = vec![1, 2, 3];
let b = vec![4, 5, 6];

let combined: Vec<i32> = a.iter()
    .chain(b.iter())
    .copied()
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Chaining multiple iterators:**
```rust
let a = vec![1, 2];
let b = vec![3, 4];
let c = vec![5, 6];

let all: Vec<i32> = a.iter()
    .chain(b.iter())
    .chain(c.iter())
    .copied()
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Mixing types (with ranges):**
```rust
let combined: Vec<i32> = vec![1, 2, 3].iter()
    .copied()
    .chain(4..7)  // Range iterator
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Common pattern - adding elements:**
```rust
let extended: Vec<i32> = std::iter::once(0)
    .chain(vec![1, 2, 3].iter().copied())
    .chain(std::iter::once(4))
    .collect();
// [0, 1, 2, 3, 4]
```

Order matters - first iterator's elements come first, then second iterator's elements.


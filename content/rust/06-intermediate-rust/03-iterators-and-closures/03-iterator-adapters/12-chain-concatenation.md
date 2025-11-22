## Chain Concatenation

What does `.chain()` do? Show how to add header/footer to a sequence.

---

`.chain()` sequentially concatenates iterators - first iterator's elements, then second's.

**Basic concatenation:**
```rust
let combined: Vec<i32> = vec![1, 2, 3].iter()
    .chain(vec![4, 5, 6].iter())
    .copied()
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Adding header and footer:**
```rust
let with_header_footer: Vec<String> = 
    std::iter::once("# Header".to_string())
        .chain(body_lines.into_iter())
        .chain(std::iter::once("# Footer".to_string()))
        .collect();
```

**Multiple chains:**
```rust
let all: Vec<i32> = first.iter()
    .chain(second.iter())
    .chain(third.iter())
    .chain(fourth.iter())
    .copied()
    .collect();
```

**Conditional chaining:**
```rust
let result: Vec<i32> = base.iter().copied()
    .chain(
        if include_extras {
            extras.iter().copied()
        } else {
            vec![].into_iter()
        }
    )
    .collect();
```

**Mixing with ranges:**
```rust
let extended: Vec<i32> = vec![1, 2, 3].iter()
    .copied()
    .chain(4..7)  // Range iterator
    .collect();
// [1, 2, 3, 4, 5, 6]
```

**Zero-cost:** Compiler eliminates chaining overhead completely.

**Order matters:** First iterator's elements come first, then second, etc. Unlike operations that can reorder, `.chain()` preserves sequence order.


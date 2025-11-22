## Take While vs Filter Difference

What's the critical difference between `.take_while()` and `.filter()`? Show an example demonstrating this.

---

**Key difference:** `.take_while()` **stops** at first failure; `.filter()` **checks every** element.

**take_while - Stops early:**
```rust
let result = (1..10)
    .take_while(|&x| x != 5)
    .collect::<Vec<_>>();
// [1, 2, 3, 4] - STOPS at 5, doesn't check 6-9
```

**filter - Checks all:**
```rust
let result = (1..10)
    .filter(|&x| x != 5)
    .collect::<Vec<_>>();
// [1, 2, 3, 4, 6, 7, 8, 9] - Skips 5 but CONTINUES
```

**Practical example:**
```rust
let lines = vec!["header", "data1", "data2", "", "data3", "data4"];

// take_while - stops at first empty line
let before_empty: Vec<_> = lines.iter()
    .take_while(|line| !line.is_empty())
    .collect();
// ["header", "data1", "data2"]

// filter - removes all empty lines
let without_empty: Vec<_> = lines.iter()
    .filter(|line| !line.is_empty())
    .collect();
// ["header", "data1", "data2", "data3", "data4"]
```

**Use take_while when:**
- Processing until sentinel value
- Reading header sections
- Collecting until condition fails
- Working with sorted/ordered data

**Use filter when:**
- Removing all unwanted elements
- Elements can appear anywhere
- Need to check entire sequence

`.take_while()` is more efficient when you know elements of interest are contiguous at the start.


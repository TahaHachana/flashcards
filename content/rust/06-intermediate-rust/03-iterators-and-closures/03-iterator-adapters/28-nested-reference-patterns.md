## Nested Reference Patterns

Why do you sometimes see `|&&x|` in filter closures? Explain the reference stacking.

---

Closures in adaptors receive references to the iterator's items, causing reference stacking.

**The pattern:**
```rust
vec![1, 2, 3].iter()
    .filter(|&&x| x > 1)  // Why double &?
    .copied()
    .collect()
```

**Understanding reference levels:**

**Starting point:**
```rust
let vec = vec![1, 2, 3];  // Vec<i32>
let iter = vec.iter();     // Iterator<Item = &i32>
```

**In `.filter()`:**
```rust
fn filter<P>(self, predicate: P)
where
    P: FnMut(&Self::Item) -> bool
    //         ^ Takes reference to Item
```

**So with `.iter()`:**
- Item is `&i32`
- Closure receives `&Item` = `&&i32`
- Hence: `|&&x|` to get `i32`

**Visual breakdown:**
```rust
vec![1, 2, 3]           // Vec<i32>
    .iter()             // Item = &i32
    .filter(|x| ...)    // x is &&i32
           //   ^^ reference to Item
           //   ^ Item itself is &i32
```

**Different patterns to handle this:**

**1. Pattern match to unpack:**
```rust
.filter(|&&x| x > 1)  // x is i32
```

**2. Explicit dereference:**
```rust
.filter(|x| **x > 1)  // **x gets to i32
```

**3. Use `.copied()` first:**
```rust
.copied()              // Item = i32
.filter(|&x| x > 1)    // x is i32 (only one &)
```

**Comparison table:**

| Iterator | Item type | Filter closure | Get i32 |
|----------|-----------|----------------|---------|
| `.into_iter()` | `i32` | `\|&x\|` | `x` |
| `.iter()` | `&i32` | `\|&&x\|` | `x` |
| `.iter_mut()` | `&mut i32` | `\|x\|` | `*x` |

**With `.map()` it's similar:**
```rust
vec.iter().map(|&x| x * 2)  // x is i32
// or
vec.iter().map(|x| *x * 2)  // *x is i32
```

**Pro tip:** When confused, let compiler infer:
```rust
vec.iter().filter(|x| {
    // Hover over x in IDE to see its type
    println!("{:?}", std::any::type_name_of_val(&x));
    **x > 1
})
```

Understanding reference levels prevents confusion and helps write idiomatic Rust.


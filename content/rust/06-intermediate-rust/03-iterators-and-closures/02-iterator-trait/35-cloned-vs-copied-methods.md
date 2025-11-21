## Cloned vs Copied Methods

What's the difference between `.cloned()` and `.copied()` iterator methods? When should you use each?

---

Both convert an iterator of references into an iterator of values, but they use different mechanisms.

**`.copied()` - For Copy types:**
```rust
fn copied(self) -> Copied<Self>
where
    Self::Item: Copy
```

**Usage:**
```rust
let numbers = vec![1, 2, 3, 4, 5];

let owned: Vec<i32> = numbers.iter()
    .copied()  // &i32 → i32 (bitwise copy)
    .collect();
```

**Works with:** `i32`, `f64`, `bool`, `char`, `&T`, and other Copy types

**`.cloned()` - For Clone types:**
```rust
fn cloned(self) -> Cloned<Self>
where
    Self::Item: Clone
```

**Usage:**
```rust
let strings = vec![String::from("a"), String::from("b")];

let owned: Vec<String> = strings.iter()
    .cloned()  // &String → String (calls .clone())
    .collect();
```

**Works with:** `String`, `Vec`, `Box`, and any Clone type

**Key differences:**

| Feature | `.copied()` | `.cloned()` |
|---------|-------------|-------------|
| Trait bound | `Copy` | `Clone` |
| Operation | Bitwise copy | Calls `.clone()` |
| Performance | Faster (memcpy) | Potentially slower (heap allocation) |
| Types | Primitives, references | All Clone types |

**Choosing between them:**

```rust
// Use .copied() for Copy types (preferred when available)
let nums: Vec<i32> = vec.iter().copied().collect();

// Use .cloned() for non-Copy types
let strings: Vec<String> = vec.iter().cloned().collect();

// Copy types work with both, but .copied() is more semantic
let nums: Vec<i32> = vec.iter().cloned().collect();  // Works but .copied() is clearer
```

**Rule of thumb:** Use `.copied()` for primitives and simple Copy types; use `.cloned()` for everything else.


## Reference Confusion in Adaptors

Explain the reference confusion issue with `.iter()` and adaptors. Why do you sometimes need `|&&x|` in closures?

---

Reference levels stack when using `.iter()` with adaptors, requiring careful dereferencing.

**The confusion:**
```rust
let numbers = vec![1, 2, 3];

// This fails
numbers.iter().map(|x| x * 2)  // ❌ Can't multiply &i32
```

**Why it happens:**

`.iter()` produces `&T`:
```rust
vec![1, 2, 3].iter()  // Iterator<Item = &i32>
```

`.map()` closure receives `&Item`:
```rust
.map(|x| ...)  // x is &&i32
```

`.filter()` closure receives `&&Item`:
```rust
.filter(|x| ...)  // x is &&&i32 if used after .iter()
```

**Solutions:**

**1. Dereference in parameter:**
```rust
numbers.iter().map(|&x| x * 2)  // x is i32
numbers.iter().filter(|&&x| x > 5)  // Need two &
```

**2. Use `.copied()` or `.cloned()`:**
```rust
numbers.iter()
    .copied()        // Converts &i32 to i32
    .map(|x| x * 2)  // x is i32
    .filter(|x| x > 5)
```

**3. Dereference in body:**
```rust
numbers.iter().map(|x| *x * 2)
numbers.iter().filter(|x| **x > 5)
```

**Pattern explanation:**
```rust
// .iter() on Vec<i32>
for x in vec.iter() {
    // x is &i32
}

// .filter() with .iter()
vec.iter().filter(|x| ...)
    // x is &&i32 (reference to &i32)
    // Need **x to get i32

// .map() with .iter()
vec.iter().map(|x| ...)
    // x is &&i32
    // But often pattern match: |&x| → x is &i32
```

**General rule:**
- Each adaptor adds one reference level to what it receives
- `.iter()` starts with references
- Pattern matching with `&` removes one level
- `*` dereference operator removes one level

**Pro tip:** Use `.copied()` early in chain to avoid this entirely.


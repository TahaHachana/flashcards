## Reference Handling in Closures

Why does this fail and what are the three ways to fix it?

```rust
let numbers = vec![1, 2, 3];
let doubled: Vec<i32> = numbers.iter()
    .map(|x| x * 2)
    .collect();
```

---

**Problem:** `.iter()` produces `&i32` references, but the closure tries to multiply a reference, which doesn't implement multiplication directly.

```rust
// ERROR: can't multiply `&i32` by `i32`
numbers.iter().map(|x| x * 2)
                    // x is &i32, not i32
```

**Fix 1: Dereference in closure parameter:**
```rust
let doubled: Vec<i32> = numbers.iter()
    .map(|&x| x * 2)  // &x dereferences to i32
    .collect();
```

**Fix 2: Use `.copied()` for Copy types:**
```rust
let doubled: Vec<i32> = numbers.iter()
    .copied()        // Copies &i32 to i32
    .map(|x| x * 2)  // Now x is i32
    .collect();
```

**Fix 3: Dereference in closure body:**
```rust
let doubled: Vec<i32> = numbers.iter()
    .map(|x| *x * 2)  // Dereference then multiply
    .collect();
```

**For non-Copy types, use `.cloned()`:**
```rust
let strings = vec![String::from("a"), String::from("b")];
let upper: Vec<String> = strings.iter()
    .cloned()                    // Clone each String
    .map(|s| s.to_uppercase())  // Now s is String
    .collect();
```

**Pattern in filter closures:**
```rust
numbers.iter()
    .filter(|&&x| x > 5)  // Double reference: &&i32
```


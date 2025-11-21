## Mutation Requires Iter Mut

Why does this fail and how do you fix it?

```rust
let mut numbers = vec![1, 2, 3];
numbers.iter().for_each(|x| *x += 10);
```

---

**Problem:** `.iter()` provides immutable references (`&T`), which can't be used to modify values.

```rust
let mut numbers = vec![1, 2, 3];

// ERROR: cannot assign to `*x` which is behind a `&` reference
numbers.iter().for_each(|x| *x += 10);
                          // x is &i32, not &mut i32
```

**Fix: Use `.iter_mut()`:**
```rust
let mut numbers = vec![1, 2, 3];

numbers.iter_mut().for_each(|x| *x += 10);
// x is now &mut i32

println!("{:?}", numbers); // [11, 12, 13]
```

**Same issue with `.map()`:**
```rust
// Wrong - can't modify through &i32
numbers.iter().map(|x| *x += 10); // ERROR

// Correct - use iter_mut
numbers.iter_mut().for_each(|x| *x += 10);
```

**In filter+modify pattern:**
```rust
numbers.iter_mut()
    .filter(|x| **x % 2 == 0)  // Read: &&mut i32 → &i32
    .for_each(|x| *x *= 10);    // Modify: &mut i32
```

**Key rule:** 
- `.iter()` → `&T` (read-only)
- `.iter_mut()` → `&mut T` (read-write)
- `.into_iter()` → `T` (take ownership)

Choose based on whether you need to modify elements in place.


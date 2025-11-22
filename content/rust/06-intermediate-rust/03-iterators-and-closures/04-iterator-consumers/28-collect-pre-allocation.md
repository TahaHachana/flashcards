## Collect Pre Allocation

How does `.collect()` optimize memory allocation? What is `size_hint()` and when does it help?

---

`.collect()` uses `size_hint()` to pre-allocate the correct amount of memory when possible.

**Size hint mechanism:**
```rust
pub trait Iterator {
    fn size_hint(&self) -> (usize, Option<usize>)
    // Returns: (lower_bound, upper_bound)
}
```

**When size is known - efficient:**
```rust
// Vec knows its size exactly
let vec = vec![1, 2, 3, 4, 5];
let collected: Vec<_> = vec.iter().collect();
// size_hint() returns (5, Some(5))
// .collect() pre-allocates exactly 5 elements
// No reallocation needed!
```

**When size is unknown - less efficient:**
```rust
// Filter doesn't know final size
let collected: Vec<_> = vec.iter()
    .filter(|&&x| x % 2 == 0)
    .collect();
// size_hint() returns (0, Some(5))
// .collect() may need to reallocate as it grows
```

**Impact on performance:**
```rust
// Known size - one allocation
(0..1000).collect::<Vec<_>>();
// Pre-allocates 1000 elements upfront

// Unknown size - multiple allocations
(0..1000)
    .filter(|x| some_condition(x))
    .collect::<Vec<_>>();
// Starts small, reallocates as needed (typically: 4, 8, 16, 32...)
```

**Adaptors that preserve size_hint:**
- `.map()` - same size as source
- `.take(n)` - size is n
- `.enumerate()` - same size as source
- `.zip()` - size is minimum of both

**Adaptors that lose size_hint:**
- `.filter()` - don't know how many pass
- `.flat_map()` - don't know expansion factor
- `.take_while()` - don't know when it stops

**Manual pre-allocation when you know size:**
```rust
let mut vec = Vec::with_capacity(expected_size);
for item in iterator {
    vec.push(item);
}
```

**Checking size hint:**
```rust
let iter = (0..100).filter(|x| x % 2 == 0);
let (lower, upper) = iter.size_hint();
println!("Will have at least {}, at most {:?}", lower, upper);
// Will have at least 0, at most Some(100)
```

**Why it matters:**
- Reallocation is expensive (copy entire vector)
- Pre-allocation avoids this overhead
- Can be 2-10x faster for large collections
- Memory locality is better with single allocation

This optimization is transparent - `.collect()` does it automatically when possible.


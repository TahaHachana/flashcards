## Filter Adaptor Characteristics

How does `.filter()` work? How does chaining multiple filters compare to a single complex predicate?

---

`.filter()` keeps only elements matching a predicate, discarding the rest.

**Signature:**
```rust
fn filter<P>(self, predicate: P) -> Filter<Self, P>
where
    P: FnMut(&Self::Item) -> bool
```

**Basic usage:**
```rust
let evens = (0..10)
    .filter(|&x| x % 2 == 0)
    .collect::<Vec<_>>();
// [0, 2, 4, 6, 8]
```

**Multiple filters:**
```rust
let result = data.iter()
    .filter(|&&x| x > 0)      // Keep positive
    .filter(|&&x| x < 100)    // Keep under 100
    .filter(|&&x| x % 2 == 0) // Keep even
    .collect::<Vec<_>>();
```

**Performance: Single pass regardless!**
```rust
// Multiple filters - SAME performance
.filter(|&x| x > 0)
.filter(|&x| x < 100)
.filter(|&x| x % 2 == 0)

// Single complex predicate - SAME performance
.filter(|&x| x > 0 && x < 100 && x % 2 == 0)
```

Both compile to checking all conditions per element in one pass.

**When to use multiple filters:**
- Readability (separate concerns)
- When conditions come from different sources
- When some filters are conditional

**Important:** Predicate receives `&Self::Item`, hence `|&&x|` with `.iter()`.


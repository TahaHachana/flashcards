## Filter Method

What does the `.filter()` method do? How does it differ from `.map()`?

---

`.filter()` keeps only elements that match a predicate (condition), discarding the rest.

**Signature:**
```rust
fn filter<P>(self, predicate: P) -> Filter<Self, P>
where
    P: FnMut(&Self::Item) -> bool
```

**Usage:**
```rust
let numbers = vec![1, 2, 3, 4, 5, 6];

let evens: Vec<i32> = numbers.iter()
    .filter(|&&x| x % 2 == 0)
    .copied()
    .collect();
// [2, 4, 6]

let long_words: Vec<&str> = words.iter()
    .filter(|word| word.len() > 5)
    .copied()
    .collect();
```

**Key differences from `.map()`:**
- `.map()`: Transforms each element (1→1)
- `.filter()`: Selects elements (n→≤n)

**Can chain multiple filters:**
```rust
vec.iter()
    .filter(|&&x| x > 0)
    .filter(|&&x| x < 10)
    .filter(|&&x| x % 2 == 0)
    .collect()
```

**Important:** Closure receives a reference to the item, hence `|&&x|` when iterating with `.iter()`.


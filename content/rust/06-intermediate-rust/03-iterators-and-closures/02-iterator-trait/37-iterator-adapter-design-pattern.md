## Iterator Adapter Design Pattern

What's the design pattern behind iterator adapters? Why are they all built on `.next()`?

---

Iterator adapters follow the **decorator pattern** - each adapter wraps an iterator and adds behavior while implementing Iterator itself.

**Core principle:**
```rust
struct Map<I, F> {
    iter: I,      // Wrapped iterator
    func: F,      // Transformation function
}

impl<I, F, B> Iterator for Map<I, F>
where
    I: Iterator,
    F: FnMut(I::Item) -> B,
{
    type Item = B;
    
    fn next(&mut self) -> Option<B> {
        self.iter.next().map(|x| (self.func)(x))
    }
}
```

**Why this works:**

1. **Composition:** Each adapter is itself an Iterator
2. **Chaining:** Can nest adapters infinitely
3. **Zero cost:** All inlines and optimizes away
4. **Type safety:** Compiler tracks entire chain

**Example chain structure:**
```rust
vec![1, 2, 3, 4, 5].iter()
    .filter(|&&x| x % 2 == 0)
    .map(|&x| x * x)
    .take(2)

// Actual nested structure:
Take<
    Map<
        Filter<
            std::slice::Iter<i32>,
            [closure]
        >,
        [closure]
    >
>
```

**Each adapter delegates to inner:**
```rust
// When you call .next() on the outermost:
Take::next() calls Map::next()
  which calls Filter::next()
    which calls Iter::next()
```

**Benefits:**

1. **Lazy evaluation:** Nothing happens until .next() is called
2. **Single pass:** Each element flows through entire chain
3. **Composable:** Any combination of adapters works
4. **Memory efficient:** No intermediate collections

**Design insight:** This pattern gives you:
- Functional programming style
- Imperative performance
- Type safety
- Zero runtime overhead

All Rust iterator methods follow this pattern, which is why they compose so elegantly and perform so well.


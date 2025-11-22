## Consumer Categories

What are the six main categories of iterator consumers? Give an example of each.

---

Iterator consumers fall into six functional categories:

**1. Collection builders** - Materialize into data structures
```rust
let vec: Vec<i32> = iter.collect();
let (evens, odds) = iter.partition(|&x| x % 2 == 0);
```

**2. Reducers** - Aggregate to single value
```rust
let sum: i32 = iter.sum();
let stats = iter.fold(initial, |acc, x| update(acc, x));
```

**3. Searchers** - Find elements or test conditions
```rust
let first = iter.find(|x| predicate(x));
let has_any = iter.any(|x| condition(x));
```

**4. Extractors** - Get specific elements
```rust
let third = iter.nth(2);
let max = iter.max();
```

**5. Counters** - Count elements
```rust
let count = iter.count();
```

**6. Side effect performers** - Execute actions
```rust
iter.for_each(|x| println!("{}", x));
```

Each category serves a different purpose in the final step of processing data.


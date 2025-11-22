## Conditional Adaptor Application

How can you conditionally apply iterator adaptors? Show patterns for dynamic pipeline construction.

---

Conditionally applying adaptors requires careful handling because different adaptors create different types.

**Problem - type mismatch:**
```rust
// This doesn't work - different types
let iter = data.iter();
let iter = if should_filter {
    iter.filter(predicate)  // Type: Filter<Iter<T>>
} else {
    iter  // Type: Iter<T>
};  // ❌ Type mismatch!
```

**Solution 1: Box<dyn Iterator>**
```rust
let iter: Box<dyn Iterator<Item = &i32>> = if should_filter {
    Box::new(data.iter().filter(predicate))
} else {
    Box::new(data.iter())
};

let result: Vec<_> = iter.collect();
```

**Solution 2: Filter with always-true predicate**
```rust
let result: Vec<_> = data.iter()
    .filter(|x| if should_filter { predicate(x) } else { true })
    .collect();
```

**Solution 3: Helper enum (Either pattern)**
```rust
enum Either<L, R> {
    Left(L),
    Right(R),
}

impl<L, R, T> Iterator for Either<L, R>
where
    L: Iterator<Item = T>,
    R: Iterator<Item = T>,
{
    type Item = T;
    fn next(&mut self) -> Option<T> {
        match self {
            Either::Left(l) => l.next(),
            Either::Right(r) => r.next(),
        }
    }
}

let iter = if should_filter {
    Either::Left(data.iter().filter(predicate))
} else {
    Either::Right(data.iter())
};
```

**Solution 4: Closure approach**
```rust
fn process_data(
    data: &[Item],
    should_filter: bool,
    should_reverse: bool
) -> Vec<Item> {
    let iter = data.iter();
    
    let iter: Box<dyn Iterator<Item = _>> = match (should_filter, should_reverse) {
        (true, true) => Box::new(iter.filter(pred).rev()),
        (true, false) => Box::new(iter.filter(pred)),
        (false, true) => Box::new(iter.rev()),
        (false, false) => Box::new(iter),
    };
    
    iter.cloned().collect()
}
```

**Solution 5: Build collection first (when small)**
```rust
let mut result: Vec<_> = data.iter().collect();

if should_filter {
    result.retain(|x| predicate(x));
}

if should_reverse {
    result.reverse();
}
```

**Trade-offs:**

| Approach | Pros | Cons |
|----------|------|------|
| Box<dyn> | Flexible | Heap allocation, dynamic dispatch |
| Always-true filter | No allocation | Slight overhead from check |
| Either enum | Zero-cost | More code |
| Collection first | Simple | Not lazy, memory usage |

**Best practice:** If conditions known at compile time, consider separate functions. If runtime, Box<dyn> is most idiomatic.


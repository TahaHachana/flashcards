## Inspect Debugging Aid

What is `.inspect()` used for? Show how to debug a multi-stage pipeline.

---

`.inspect()` allows peeking at values flowing through a pipeline without affecting them - primarily for debugging.

**Signature:**
```rust
fn inspect<F>(self, f: F) -> Inspect<Self, F>
where
    F: FnMut(&Self::Item)
```

**Debugging pipeline stages:**
```rust
let result: Vec<i32> = numbers.iter()
    .inspect(|x| println!("Before filter: {}", x))
    .filter(|&&x| x % 2 == 0)
    .inspect(|x| println!("After filter: {}", x))
    .map(|&x| x * x)
    .inspect(|x| println!("After map: {}", x))
    .collect();
```

**Output shows execution flow:**
```
Before filter: 1
Before filter: 2
After filter: 2
After map: 4
Before filter: 3
Before filter: 4
After filter: 4
After map: 16
...
```

**Logging with context:**
```rust
let processed = data.iter()
    .inspect(|x| debug!("Processing: {:?}", x))
    .map(expensive_operation)
    .inspect(|x| debug!("Completed: {:?}", x))
    .collect();
```

**Counting processed elements:**
```rust
let mut count = 0;
let result: Vec<_> = iter
    .inspect(|_| count += 1)
    .filter(predicate)
    .collect();
println!("Processed {} elements", count);
```

**Validation during iteration:**
```rust
let validated: Vec<_> = items.iter()
    .inspect(|item| assert!(item.is_valid()))
    .map(|item| item.process())
    .collect();
```

**Key characteristics:**
- Takes `&Item` (reference, not ownership)
- Returns same iterator type
- No transformation of values
- Used for side effects
- Removed in release builds with optimization

Perfect for understanding lazy evaluation and debugging complex chains.


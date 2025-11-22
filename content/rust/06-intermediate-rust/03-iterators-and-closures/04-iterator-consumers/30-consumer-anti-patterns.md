## Consumer Anti Patterns

What are common anti-patterns when using consumers? Show the mistake and correction for each.

---

Common mistakes that hurt performance or clarity:

**Anti-pattern 1: Collect-then-length check**
```rust
// ❌ Wrong - allocates unnecessarily
if data.iter().filter(p).collect::<Vec<_>>().is_empty() { }

// ✅ Right - no allocation
if data.iter().filter(p).next().is_none() { }
// or
if !data.iter().any(p) { }
```

**Anti-pattern 2: Unnecessary intermediate Vec**
```rust
// ❌ Wrong - two allocations
let result: Vec<_> = data.iter()
    .map(|x| x * 2)
    .collect::<Vec<_>>()
    .iter()
    .filter(|&&x| x > 10)
    .collect();

// ✅ Right - single allocation
let result: Vec<_> = data.iter()
    .map(|x| x * 2)
    .filter(|&x| x > 10)
    .collect();
```

**Anti-pattern 3: Multiple passes for aggregations**
```rust
// ❌ Wrong - three passes through data
let sum: i32 = data.iter().sum();
let count = data.iter().count();
let avg = sum / count;

// ✅ Right - single pass
let (sum, count) = data.iter()
    .fold((0, 0), |(s, c), &x| (s + x, c + 1));
let avg = sum / count;
```

**Anti-pattern 4: Collecting when you need count**
```rust
// ❌ Wrong - allocates Vec just to count
let count = data.iter()
    .filter(p)
    .collect::<Vec<_>>()
    .len();

// ✅ Right - just counts
let count = data.iter()
    .filter(p)
    .count();
```

**Anti-pattern 5: Wrong consumer for boolean check**
```rust
// ❌ Wrong - checks all elements
if data.iter().filter(|x| x.is_valid()).count() > 0 { }

// ✅ Right - short-circuits
if data.iter().any(|x| x.is_valid()) { }
```

**Anti-pattern 6: Forgetting consumer entirely**
```rust
// ❌ Wrong - does nothing!
data.iter()
    .map(|x| expensive_operation(x));

// ✅ Right - actually executes
data.iter()
    .map(|x| expensive_operation(x))
    .for_each(|result| process(result));
```

**Anti-pattern 7: Inefficient max/min**
```rust
// ❌ Wrong - sorts entire collection
let max = data.iter()
    .copied()
    .collect::<Vec<_>>()
    .sort()
    .last();

// ✅ Right - single pass
let max = data.iter().max();
```

**Anti-pattern 8: Recreating same iterator**
```rust
// ❌ Wrong - repeats expensive chain
fn process() {
    let x = expensive_chain().find(p1);
    let y = expensive_chain().find(p2);
    let z = expensive_chain().count();
}

// ✅ Right - compute once
fn process() {
    let collected: Vec<_> = expensive_chain().collect();
    let x = collected.iter().find(p1);
    let y = collected.iter().find(p2);
    let z = collected.len();
}
```

**Golden rule:** Use the most specific consumer that solves your problem - avoid over-generalizing to collect().


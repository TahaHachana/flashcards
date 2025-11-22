## Choosing Right Consumer

Show examples of inefficient consumer choices and their efficient alternatives.

---

Choosing the right consumer significantly impacts performance and code clarity.

**Inefficient: Using collect when you need boolean**
```rust
// BAD - unnecessary allocation
let has_valid = data.iter()
    .filter(|x| x.is_valid())
    .collect::<Vec<_>>()
    .len() > 0;

// GOOD - short-circuits
let has_valid = data.iter()
    .any(|x| x.is_valid());
```

**Inefficient: Collecting then counting**
```rust
// BAD - allocates vector unnecessarily
let count = data.iter()
    .filter(predicate)
    .collect::<Vec<_>>()
    .len();

// GOOD - just counts
let count = data.iter()
    .filter(predicate)
    .count();
```

**Inefficient: Collecting to check emptiness**
```rust
// BAD - processes all elements
if data.iter().collect::<Vec<_>>().is_empty() { }

// GOOD - checks just first element
if data.iter().next().is_none() { }

// EVEN BETTER - direct check if available
if data.is_empty() { }
```

**Inefficient: Manual fold for sum/product**
```rust
// BAD - verbose and harder to read
let sum = data.iter().fold(0, |acc, &x| acc + x);

// GOOD - specialized consumer
let sum: i32 = data.iter().sum();
```

**Inefficient: Collecting when you need one element**
```rust
// BAD - processes everything, allocates
let first_valid = data.iter()
    .filter(is_valid)
    .collect::<Vec<_>>()[0];

// GOOD - stops at first
let first_valid = data.iter()
    .find(is_valid)
    .unwrap();
```

**Inefficient: Multiple collects for multiple consumers**
```rust
// BAD - processes chain multiple times
let vec1: Vec<_> = source.iter().filter(p).collect();
let vec2: Vec<_> = source.iter().filter(p).collect();

// GOOD - process once, clone source
let filtered: Vec<_> = source.iter().filter(p).collect();
let vec1 = filtered.clone();
let vec2 = filtered;
```

**Decision tree:**
- Need all elements in collection → `.collect()`
- Need single numeric value → `.sum()`, `.product()`, `.fold()`
- Need to find element → `.find()`, `.position()`
- Need boolean test → `.any()`, `.all()`
- Need count → `.count()`
- Need side effects only → `.for_each()`


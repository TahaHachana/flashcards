## Consumer Ownership

Why can't you use an iterator after calling a consumer? What's the ownership rule?

---

Consumers take ownership of the iterator (`self`), making it unavailable after use.

**The problem:**
```rust
let iter = vec![1, 2, 3].iter();

let sum: i32 = iter.sum();  // Consumes iter
// let count = iter.count();  // ERROR: value used after move
```

**Error message:**
```
error[E0382]: use of moved value: `iter`
  |
  | let sum: i32 = iter.sum();
  |                ---- value moved here
  | let count = iter.count();
  |             ^^^^ value used here after move
```

**Why this happens - signature:**
```rust
// Consumer takes self (not &self)
fn sum<S>(self) -> S  // Takes ownership!

// Compare to adaptor
fn map<F>(self, f: F) -> Map<Self, F>  // Also takes self, but returns iterator
```

**Solution 1: Create multiple iterators from source:**
```rust
let vec = vec![1, 2, 3];

let sum: i32 = vec.iter().sum();
let count = vec.iter().count();
let max = vec.iter().max();
// Each creates new iterator from vec
```

**Solution 2: Clone the iterator (if possible):**
```rust
let iter = vec.iter();

let sum: i32 = iter.clone().sum();
let count = iter.count();  // Original still available
```

**Solution 3: Collect first, then reuse:**
```rust
let processed: Vec<_> = source.iter()
    .filter(predicate)
    .map(transform)
    .collect();

// Now can do multiple operations
let sum = processed.iter().sum();
let count = processed.len();
let max = processed.iter().max();
```

**Why ownership is taken:**
Consumers genuinely consume the iterator - they might need to drain it completely, and leaving it in an intermediate state would be problematic.

**Mental model:** Consumers are terminal - they end the chain by consuming it.


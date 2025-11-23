## Iterator Trait Requirements

What are the two requirements for implementing the Iterator trait? What do you get for free?

---

Only two things are required to implement Iterator:

**1. Associated type `Item`:**
```rust
type Item = YourType;
```
Specifies what type the iterator yields.

**2. Method `next(&mut self)`:**
```rust
fn next(&mut self) -> Option<Self::Item>;
```
Defines how to produce the next element.

**Trait structure:**
```rust
pub trait Iterator {
    type Item;  // Required
    
    fn next(&mut self) -> Option<Self::Item>;  // Required
    
    // 70+ provided methods for free:
    fn map<F>(self, f: F) -> Map<Self, F> { /* ... */ }
    fn filter<P>(self, predicate: P) -> Filter<Self, P> { /* ... */ }
    fn collect<B>(self) -> B { /* ... */ }
    fn sum<S>(self) -> S { /* ... */ }
    // ... and many more
}
```

**What you get for free:**
- All adaptors (map, filter, take, skip, enumerate, zip, etc.)
- All consumers (collect, sum, fold, count, find, any, all, etc.)
- For loop support (with IntoIterator)
- Iterator combinators (chain, flatten, etc.)

**Example:**
```rust
struct Counter { count: u32, max: u32 }

impl Iterator for Counter {
    type Item = u32;
    
    fn next(&mut self) -> Option<u32> {
        if self.count < self.max {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}

// Now Counter has ALL iterator methods automatically!
let sum: u32 = Counter { count: 0, max: 5 }.sum();
let doubled: Vec<_> = Counter { count: 0, max: 3 }
    .map(|x| x * 2)
    .collect();
```

Implement two things, get 70+ methods free.


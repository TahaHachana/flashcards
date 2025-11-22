## Consumer Chain Ending

Why must consumers be at the end of an iterator chain? Can you chain after a consumer?

---

Consumers are terminal operations - they return values, not iterators, ending the chain.

**Can't chain after consumer:**
```rust
// ERROR: consumers return values, not iterators
let result = data.iter()
    .filter(predicate)
    .sum()           // Returns i32
    .map(|x| x * 2); // Can't call .map() on i32!
```

**Why:**
```rust
// Adaptor signature - returns Iterator
fn map<F>(self, f: F) -> Map<Self, F>
//                       ^^^^^^^^^^^^^^ Returns iterator

// Consumer signature - returns Value  
fn sum<S>(self) -> S
//                 ^ Returns concrete type, not iterator
```

**Correct structure:**
```rust
// Adaptors first, consumer last
let result: Vec<_> = data.iter()
    .filter(predicate)    // Adaptor → Iterator
    .map(transform)       // Adaptor → Iterator
    .take(10)            // Adaptor → Iterator
    .collect();          // CONSUMER → Vec
```

**Can't do this:**
```rust
// ERROR: Can't continue after collecting
data.iter()
    .collect::<Vec<_>>()
    .iter()              // This needs a new iterator from Vec
    .map(|x| x * 2)
```

**Must restart from collection:**
```rust
// Correct: collect, then create new iterator
let collected: Vec<_> = data.iter().collect();
let transformed: Vec<_> = collected.iter()
    .map(|x| x * 2)
    .collect();
```

**Multiple consumers require separate chains:**
```rust
// Can't do: iter.sum().count() 

// Must do:
let sum: i32 = data.iter().sum();
let count = data.iter().count();
```

**Mental model:**

```
Source → Adaptor → Adaptor → Adaptor → CONSUMER
  ↓         ↓         ↓         ↓          ↓
Iterator  Iterator  Iterator  Iterator   Value
                                          (END)
```

**Why this design:**
- Consumers genuinely consume the iterator
- Return value is the final result
- No iterator state to continue from
- Forces clear, linear data flow

Consumers are exits, not waypoints.


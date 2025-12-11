## Gotcha - Forgetting Guards are Held

What's the problem with holding RefCell guards too long? Show the gotcha and solution.

---

**The gotcha:**
```rust
use std::cell::RefCell;

let cell = RefCell::new(vec![1, 2, 3]);

// ❌ Guard held too long
let borrow = cell.borrow();
println!("{:?}", borrow);
// ... lots of code ...
// cell.borrow_mut();  // Would panic! borrow still held

// ... more code ...
println!("{:?}", borrow);  // Still using guard
```

**Problem:** The immutable borrow (`borrow`) lives until end of scope, blocking mutable borrows.

**Solution 1: Explicit scopes**
```rust
// ✅ Drop guard early
{
    let borrow = cell.borrow();
    println!("{:?}", borrow);
}  // Guard dropped here

cell.borrow_mut();  // OK now
```

**Solution 2: Don't store guards**
```rust
// ✅ Use and drop immediately
println!("{:?}", cell.borrow());  // Guard dropped after line

cell.borrow_mut();  // OK
```

**Solution 3: Explicit drop**
```rust
let borrow = cell.borrow();
println!("{:?}", borrow);
drop(borrow);  // Explicitly release

cell.borrow_mut();  // OK
```

**Rule:** Keep guard lifetimes as short as possible.


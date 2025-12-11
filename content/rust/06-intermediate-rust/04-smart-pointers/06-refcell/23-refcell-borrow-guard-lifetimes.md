## RefCell Borrow Guard Lifetimes

Explain the lifetime behavior of `Ref` and `RefMut` guards. How long do they live?

---

**Guards live until dropped:**

```rust
use std::cell::RefCell;

let cell = RefCell::new(vec![1, 2, 3]);

// Guard created
let guard = cell.borrow();
println!("{:?}", guard);

// ... guard still alive ...
// cell.borrow_mut();  // Would panic - guard still exists

// Guard dropped at end of scope
// Now can borrow again
```

**Lifetime is lexical scope:**
```rust
{
    let guard = cell.borrow();
    // guard lives here
}  // guard dropped

cell.borrow_mut();  // OK now
```

**Early drop:**
```rust
let guard = cell.borrow();
println!("{:?}", guard);
drop(guard);  // Explicitly drop

cell.borrow_mut();  // OK - guard gone
```

**No drop needed:**
```rust
// Guard created and dropped in same expression
println!("{:?}", cell.borrow());
// Already dropped!

cell.borrow_mut();  // OK
```

**Key insight:** Guards follow RAII (Resource Acquisition Is Initialization):
- Created when you call `.borrow()`/`.borrow_mut()`
- Automatically track active borrows
- Automatically release when dropped
- Can't violate rules while guard exists

**Pattern:** Keep guard lifetimes as short as possible to avoid conflicts.


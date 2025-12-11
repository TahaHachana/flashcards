## Gotcha - Double Borrow in Same Expression

What's wrong with borrowing a RefCell multiple times in the same expression? Show the gotcha and fix.

---

**The gotcha:**
```rust
use std::cell::RefCell;

let cell = RefCell::new(vec![1, 2, 3]);

// ⚠️ This might panic!
cell.borrow_mut().push(*cell.borrow().first().unwrap());
//   └─ mutable ─┘       └─ immutable ─┘
// Both borrows active at same time!
```

**Why it panics:**
1. `cell.borrow_mut()` creates mutable borrow
2. Then `cell.borrow()` tries immutable borrow
3. Can't have both at same time
4. Runtime panic!

**Solution: Separate the borrows**
```rust
// ✅ Correct: separate borrows
let first = *cell.borrow().first().unwrap();
// Immutable borrow dropped here

cell.borrow_mut().push(first);
// Mutable borrow happens after immutable is done
```

**Another example:**
```rust
// ❌ Bad
let sum = *cell.borrow() + *cell.borrow();

// ✅ Good
let value = *cell.borrow();
let sum = value + value;
```

**Rule:** Don't borrow the same RefCell multiple times in one expression.


## Gotcha - Rc Doesn't Allow Direct Mutation

Why can't you directly mutate data in `Rc`, and what's the pattern to work around this?

---

**The problem:**
```rust
use std::rc::Rc;

let data = Rc::new(vec![1, 2, 3]);

// ❌ Cannot mutate
// data.push(4);  // Error: Rc<Vec> doesn't have push
```

**Why?** `Rc` only provides shared immutable access (`&T`). Multiple owners with mutable access would violate aliasing rules.

**Solution 1: Rc<RefCell<T>> pattern:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

let data = Rc::new(RefCell::new(vec![1, 2, 3]));
let data2 = Rc::clone(&data);

// Mutate through RefCell
data.borrow_mut().push(4);

// Both see the change
println!("{:?}", data.borrow());   // [1, 2, 3, 4]
println!("{:?}", data2.borrow());  // [1, 2, 3, 4]
```

**Solution 2: Make the Rc itself mutable:**
```rust
let mut data = Rc::new(vec![1, 2, 3]);

// Replace entire Rc
data = Rc::new(vec![4, 5, 6]);
// Old data dropped if no other Rc's exist
```

**Pattern:** `Rc<RefCell<T>>` is standard for shared mutable state (single-threaded).


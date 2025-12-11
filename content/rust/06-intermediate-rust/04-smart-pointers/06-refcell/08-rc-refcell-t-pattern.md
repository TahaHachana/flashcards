## Rc<RefCell<T>> Pattern

Why is `Rc<RefCell<T>>` a common pattern? What does each layer provide?

---

**The combination provides:**
- **Shared ownership** (from Rc)
- **Interior mutability** (from RefCell)

**Example:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

fn main() {
    let data = Rc::new(RefCell::new(vec![1, 2, 3]));
    
    // Multiple owners
    let data2 = Rc::clone(&data);
    let data3 = Rc::clone(&data);
    
    // All can mutate
    data.borrow_mut().push(4);
    data2.borrow_mut().push(5);
    data3.borrow_mut().push(6);
    
    println!("{:?}", data.borrow());  // [1, 2, 3, 4, 5, 6]
}
```

**Why you need both:**
- `Rc<T>` alone: Can share, but immutable
- `RefCell<T>` alone: Can mutate, but single owner
- `Rc<RefCell<T>>`: Can share AND mutate ✓

**Understanding the layers:**
```
Rc<RefCell<Vec<i32>>>
│
├─ Rc: Multiple ownership (reference counting)
│
└─ RefCell: Interior mutability (runtime borrow checking)
   │
   └─ Vec<i32>: The actual data
```

**Standard pattern** for shared mutable state in single-threaded contexts.


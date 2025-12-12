## Weak References Solution

How do `Weak` references solve reference cycles? Show the solution pattern.

---

**Weak references don't keep data alive** - they don't contribute to the strong count.

**Solution pattern:**
```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct Node {
    value: i32,
    next: RefCell<Option<Rc<Node>>>,      // Strong (forward)
    prev: RefCell<Option<Weak<Node>>>,    // Weak (backward)
}

fn main() {
    let node1 = Rc::new(Node {
        value: 1,
        next: RefCell::new(None),
        prev: RefCell::new(None),
    });
    
    let node2 = Rc::new(Node {
        value: 2,
        next: RefCell::new(None),
        prev: RefCell::new(Some(Rc::downgrade(&node1))),  // Weak!
    });
    
    *node1.next.borrow_mut() = Some(Rc::clone(&node2));
    
    // No cycle! Weak doesn't prevent cleanup
    println!("node1 strong: {}", Rc::strong_count(&node1));  // 1
    println!("node1 weak: {}", Rc::weak_count(&node1));      // 1
}
```

**Pattern for bidirectional references:**
- Parent → Child: Strong (`Rc`)
- Child → Parent: Weak (`Weak`)
- Forward: Strong (`Rc`)
- Backward: Weak (`Weak`)

**Using Weak:**
```rust
let rc = Rc::new(5);
let weak: Weak<i32> = Rc::downgrade(&rc);

// Must upgrade to use (might fail)
match weak.upgrade() {
    Some(rc) => println!("Data: {}", rc),
    None => println!("Data was dropped"),
}
```

**Rule:** Use Weak for back-references to break cycles.


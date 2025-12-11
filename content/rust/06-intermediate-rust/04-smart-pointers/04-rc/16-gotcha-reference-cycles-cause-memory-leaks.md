## Gotcha - Reference Cycles Cause Memory Leaks

Demonstrate a reference cycle memory leak and show the fix using `Weak`.

---

**The leak:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    next: Option<Rc<RefCell<Node>>>,
}

fn main() {
    let node1 = Rc::new(RefCell::new(Node { next: None }));
    let node2 = Rc::new(RefCell::new(Node {
        next: Some(Rc::clone(&node1)),
    }));
    
    // Create cycle
    node1.borrow_mut().next = Some(Rc::clone(&node2));
    
    println!("node1: {}", Rc::strong_count(&node1));  // 2
    println!("node2: {}", Rc::strong_count(&node2));  // 2
    
    // ⚠️ Memory leaked! Both have count = 2, never freed
}
```

**The fix:**
```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct Node {
    next: Option<Rc<RefCell<Node>>>,      // Strong
    prev: Option<Weak<RefCell<Node>>>,    // Weak
}

fn main() {
    let node1 = Rc::new(RefCell::new(Node {
        next: None,
        prev: None,
    }));
    
    let node2 = Rc::new(RefCell::new(Node {
        next: None,
        prev: Some(Rc::downgrade(&node1)),  // Weak reference
    }));
    
    node1.borrow_mut().next = Some(Rc::clone(&node2));
    
    // ✅ No cycle! Weak doesn't prevent cleanup
}
```

**Pattern:** Use `Weak` for "parent" or "back" pointers to break cycles.


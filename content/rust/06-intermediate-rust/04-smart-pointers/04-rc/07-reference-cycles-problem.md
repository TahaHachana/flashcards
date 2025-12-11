## Reference Cycles Problem

What is a reference cycle with `Rc`, why does it cause a memory leak, and how do you detect it?

---

A **reference cycle** occurs when two or more `Rc` pointers point at each other, preventing the count from ever reaching zero.

**Example of a cycle:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    next: Option<Rc<RefCell<Node>>>,
}

let node1 = Rc::new(RefCell::new(Node { next: None }));
let node2 = Rc::new(RefCell::new(Node { 
    next: Some(Rc::clone(&node1))  // node2 → node1
}));

// Create cycle: node1 → node2
node1.borrow_mut().next = Some(Rc::clone(&node2));

// ⚠️ Memory leak!
```

**Why it leaks:**
- `node1` count: 2 (original + node2's reference)
- `node2` count: 2 (original + node1's reference)
- When both go out of scope, each drops one reference
- Both still have count = 1, so neither is freed!

**Detection:**
```rust
println!("node1 count: {}", Rc::strong_count(&node1));  // 2
println!("node2 count: {}", Rc::strong_count(&node2));  // 2
// If count never reaches 1 after expected drops, you may have a cycle
```

**Solution:** Use `Weak` references to break cycles.


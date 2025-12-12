## Reference Cycles Problem

What is a reference cycle with `Rc`, why does it cause a memory leak, and how do you detect it?

---

**What is a reference cycle?**
When two or more `Rc` pointers reference each other, creating a loop that prevents the reference count from ever reaching zero.

**Example:**
```rust
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
    next: RefCell<Option<Rc<Node>>>,
}

fn main() {
    let node1 = Rc::new(Node {
        next: RefCell::new(None),
    });
    
    let node2 = Rc::new(Node {
        next: RefCell::new(Some(Rc::clone(&node1))),
    });
    
    // Create cycle: node1 → node2 → node1
    *node1.next.borrow_mut() = Some(Rc::clone(&node2));
    
    // Memory leak!
}
```

**Why it leaks:**
```
After cycle creation:
- node1: count = 2 (local + node2's reference)
- node2: count = 2 (local + node1's reference)

After scope ends:
- node1: count = 1 (node2's reference remains)
- node2: count = 1 (node1's reference remains)

Neither reaches count = 0, so neither is freed!
```

**Detection:**
```rust
println!("node1 count: {}", Rc::strong_count(&node1));  // 2
println!("node2 count: {}", Rc::strong_count(&node2));  // 2

// If counts don't decrease as expected after drops, investigate cycles
```

**Tools:**
- Valgrind: `valgrind --leak-check=full ./program`
- Address Sanitizer
- Memory profilers (heaptrack, massif)


## Tree with Weak Parent Pointers

Demonstrate using `Weak` to create a tree with parent pointers that doesn't leak memory.

---

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct TreeNode {
    value: i32,
    children: RefCell<Vec<Rc<TreeNode>>>,
    parent: RefCell<Weak<TreeNode>>,  // Weak prevents cycles
}

impl TreeNode {
    fn new(value: i32) -> Rc<Self> {
        Rc::new(TreeNode {
            value,
            children: RefCell::new(vec![]),
            parent: RefCell::new(Weak::new()),
        })
    }
    
    fn add_child(parent: &Rc<TreeNode>, child: Rc<TreeNode>) {
        // Set child's parent (weak reference)
        *child.parent.borrow_mut() = Rc::downgrade(parent);
        
        // Add child to parent (strong reference)
        parent.children.borrow_mut().push(child);
    }
}

fn main() {
    let root = TreeNode::new(1);
    let child1 = TreeNode::new(2);
    let child2 = TreeNode::new(3);
    
    TreeNode::add_child(&root, child1);
    TreeNode::add_child(&root, child2);
    
    // No leaks - weak references don't create cycles
}
```

**Why no cycle:**
- Parent → Child: Strong (parent owns children)
- Child → Parent: Weak (doesn't keep parent alive)
- When root dropped, children can be freed
- Weak references don't prevent cleanup

**Memory cleanup order:**
1. Root goes out of scope
2. Strong count to root becomes 0
3. Root freed, drops children strong refs
4. Children freed (weak parent refs don't matter)


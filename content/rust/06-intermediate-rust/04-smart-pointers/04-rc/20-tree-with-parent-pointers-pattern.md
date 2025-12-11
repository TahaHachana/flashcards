## Tree with Parent Pointers Pattern

Implement a tree node with both parent and child pointers using `Rc` and `Weak` to avoid cycles.

---

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct TreeNode {
    value: i32,
    parent: RefCell<Weak<TreeNode>>,           // Weak to parent
    children: RefCell<Vec<Rc<TreeNode>>>,      // Strong to children
}

impl TreeNode {
    fn new(value: i32) -> Rc<Self> {
        Rc::new(TreeNode {
            value,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![]),
        })
    }
    
    fn add_child(parent: &Rc<TreeNode>, child: Rc<TreeNode>) {
        // Set child's parent (weak reference)
        *child.parent.borrow_mut() = Rc::downgrade(parent);
        // Add child to parent's children (strong reference)
        parent.children.borrow_mut().push(child);
    }
}

fn main() {
    let root = TreeNode::new(1);
    let child1 = TreeNode::new(2);
    let child2 = TreeNode::new(3);
    
    TreeNode::add_child(&root, child1);
    TreeNode::add_child(&root, child2);
    
    // ✅ No cycle! Parent→child is strong, child→parent is weak
}
```

**Pattern:**
- **Downward (parent→child)**: Strong `Rc` (parents own children)
- **Upward (child→parent)**: Weak (children don't own parents)
- Prevents cycles while allowing bidirectional traversal


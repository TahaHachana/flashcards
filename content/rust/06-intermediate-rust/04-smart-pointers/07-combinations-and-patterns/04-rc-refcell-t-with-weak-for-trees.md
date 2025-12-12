## Rc<RefCell<T>> with Weak for Trees

Show how to use `Rc<RefCell<T>>` with `Weak` to build a tree with parent pointers that doesn't leak memory.

---

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

struct TreeNode {
    value: i32,
    children: RefCell<Vec<Rc<TreeNode>>>,
    parent: RefCell<Weak<TreeNode>>,  // Weak to avoid cycles
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
        
        // Add child to parent
        parent.children.borrow_mut().push(child);
    }
}

fn main() {
    let root = TreeNode::new(1);
    let child1 = TreeNode::new(2);
    let child2 = TreeNode::new(3);
    
    TreeNode::add_child(&root, child1);
    TreeNode::add_child(&root, child2);
}
```

**Pattern notes:**
- Children → `Rc` (parent owns children)
- Parent pointer → `Weak` (prevents reference cycles)
- Both use `RefCell` (tree structure changes)

**Why Weak?** Prevents cycle: parent → child (strong) and child → parent (weak) means parent can be freed when no other references exist.

